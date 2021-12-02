import requests 
input = 'https://adventofcode.com/2021/day/2/input'
resp = requests.get(input)
resp.content