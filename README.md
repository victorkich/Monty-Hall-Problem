<h1 align="center">Monty Hall Problem</h1>
<h3 align="center">Simulation for Monty Hall problem with the ability to run millions of tests in seconds.</h3>

<p align="center"> 
  <img src="https://img.shields.io/badge/Numpy-v1.18.2-blue"/>
  <img src="https://img.shields.io/badge/Tqdm-v4.42.1-blue"/>
</p>
<br/>

## Environment
<p align="justify"> 
  <img src="media/montyhall.png" alt="MontyHall" align="right" width="320">
  <a>The environment is very simple, done entirely in python and numpy. It is possible to configure the number of tests by changing the global variable LOOP_SIZE or change the initial 'seed' of the doors by changing the global variable SEED. This project only took into consideration the use of 3 doors, to use more doors the code should be remade.</a>
</p>
  

## Setup
<p align="justify"> 
 <a>All of requirements is show in the badgets above, but if you want to install all of them, enter the repository and execute the following line of code:</a>
</p>

```shell
pip3 install -r requirements.txt
```

<p align="justify"> 
 <a>To execute the code just use:</a>
</p>

```shell
python3 monty_hall.py
```

## Objectives
<p align="justify"> 
  This problem consists in a game where we have 3 doors, two of these doors are empty and one has a prize. The player must choose a door to his liking and then one of the doors that was not chosen by the player and that does not have the prize will be opened leaving the player with two options: continue with his door or change to the other door. It's common sense to believe that only because you have two doors the chance of hitting is 50%.

This project aims to demonstrate that the best choice for the second stage is to switch to the other door. And this can be demonstrated by this simulation, bringing a very big gain by making this choice, where the chance of hit goes from 33% to 66%.
</p>

<p align="center"> 
  <img src="media/montyhall.gif" alt="MontyHall"/>
</p>  

<p align="center"> 
  <i>If you liked this repository, please don't forget to starred it!</i>
  <img src="https://img.shields.io/github/stars/victorkich/Monty-Hall-Problem?style=social"/>
</p>
