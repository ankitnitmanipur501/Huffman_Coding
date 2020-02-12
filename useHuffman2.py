# -*- coding: utf-8 -*-
"""
Created on Wed sep  6 :35:18 2019

@author: ankit_singh
"""

from huffman2 import huffmanCoding

path='D:\BTECH\Projects\HuffmanCodingPractice\sample.txt'
file=huffmanCoding(path)
print('Compressing , please wait!!')
compressed_file_path=file.compress()
print('Location of compressed file : ',compressed_file_path)
print()
print('Decompressing , please wait!!')
decompressed_file_path=file.decompress(compressed_file_path)
print('Location of decompressed file : ',decompressed_file_path)