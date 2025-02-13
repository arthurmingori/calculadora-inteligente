#!/bin/bash

#Cabeçario


echo "Você está no diretório $PWD"

echo "Seja bem-vindo a Calculadora Inteligente"

#Instalação do Python, caso a pessoa não o possua

echo "Instalando/atualizando o sistema Python"

./install_python.sh

#Executa o código Python

python3 /home/arthur/modulo1/calculadora/calc.py



