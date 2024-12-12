{
inputs.poetry2nix.url = "github:nix-community/poetry2nix";


outputs = { self, nixpkgs, poetry2nix }:

let
  system = "x86_64-linux";
  pkgs = nixpkgs.legacyPackages.${system};

  pypkgs-build-requirements = {
    customtkinter = [ "setuptools" ];
    tkintermapview = [ "setuptools" ];
  };

  p2n-overrides = defaultPoetryOverrides.extend (self: super:
    builtins.mapAttrs (package: build-requirements:
      (builtins.getAttr package super).overridePythonAttrs (old: {
        buildInputs = (old.buildInputs or [ ]) ++ (builtins.map (pkg: if builtins.isString pkg then builtins.getAttr pkg super else pkg) build-requirements);
      })
    ) pypkgs-build-requirements
  );

  inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication mkPoetryEnv defaultPoetryOverrides;
  pythonApp = mkPoetryApplication { projectDir = ./.; };
  pythonEnv = mkPoetryEnv {
    projectDir = ./.;
    overrides = p2n-overrides;
  };


in {
  devShells.${system}.default = pkgs.mkShell {
    packages = [
      pkgs.python312Full
      pythonEnv
    ];
  };
};
}
