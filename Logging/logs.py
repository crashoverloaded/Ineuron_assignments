import logging as lg

# Logging information in a file
# Please check the IPYNB file in which logging and debugging is explained in Ineuron folder in /home
lg.basicConfig(filename="test.log",level = lg.INFO)
lg.info("Hello world in Logging")
