# Almaz Suleymanov' comparing of efficiency of distributed and synchronous calculations

## Purpose

Compare the efficiency and speed for those two types of calculations:
1. **Synchronous**: the simplest straightforward way to do calculations without using threads, etc
2. **Distributed**: not that easy as this approach has to handle all the network communications and synchronisation of multiple calculating units

## Prerequisites for unit (the remote machine)
* docker engine installed
* public IPv4 (see config.py) 
> you can use my ready to go server (see config.py:UNIT_IP)

## Run

**Local machine**:
1. `pip install -r requirements.txt`
2. `python3 test_calculations.py`

**Unit (remote machine)**:
1. `docker compose up -d`