# GPS Graph
*Noé LORRET-DESPRET*<br>
*Laure WARLOP*<br>
*CIR3*<br>

## Context
Graphs<br>
Optimizations ?<br>
Contraintes utilisateurs (changement initéraires, multi-moyen-locomotion)<br>
Openstreetmap (comment fetch / quoi fetch ?)<br>
OSMnX / NetworkX<br>

## Goal
We will build a GPS<br>
Caen and at multiple transportation modes (car, walking...)<br>
Using a graph to represent a city (Node are point of interest, edges are roads)<br>
Users can add "warnings" (road blocked, traffic jam...) that change the path or time to arrive at destination<br>
User friendly interface<br>
<br>
**<u>Problem solved by the project:</u>**<br>
How to travel the fastest from A to B in a city ?<br>


## Organisation
Interface - wrlp<br>
API Openstreetmap - Skoh<br>
Bridge - Skoh<br>
Graphs - wrlp<br>
Core - both<br>
<br>
Chacun une branche<br>
Merge sur le main tous les 2-3 soirs<br>
