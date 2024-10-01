from .base import Base
from src.utils import random_element


class SendCoffee(Base):
    name = 'cafe'
    aliases = ['coffee', 'cafezinho', 'café']
    stickers = [
        'CAACAgEAAx0CX8bCxAADrmGxea08Pep5Otyd26YgZJjH3hlEAAJ-AAPFWAYJwz3qe466JLYjBA',
        'CAACAgEAAx0CX8bCxAADr2GxehObVS3YbEf_cnX90wRnVsm-AAIDAQAC8PrXP4LFqo9gPCoeIwQ',
        'CAACAgEAAx0CX8bCxAADsGGxeo4DCRonBydxt4k03jWoYdg9AAKFAQACRV8HL-h6NTHB7jjdIwQ',
        'CAACAgIAAx0CX8bCxAADsWGxesiEPQTrCViBO3WRioPW0_VEAAI1VwACns4LAAFiq1HybYdw8iME',
        'CAACAgEAAx0CX8bCxAADsmGxe29XLDEKtZ-QRkx3azuIWwksAALiAQACRV8HL_lTFRSjL4p1IwQ',
        'CAACAgEAAxkBAAEBlLpjtLVhkvY9Afr5jF2SocRDw9IPKQAC6iIAAnj8xgVQXLC3zNAWIi0E',
        'CAACAgIAAxkBAAEBlL5jtLWGrUQEErtEyajgad7U4jcd5gACAwADJjOjO-tKknyN0BcmLQQ',
        'CAACAgEAAxkBAAEBlMJjtLW1lVfjxQnJnSzMb5jY4AEW1QACEAADLGnfHSdJEqBB9sR_LQQ',
        'CAACAgEAAxkBAAEBlMZjtLXZY5hljYZC6JdAbjNNCNgQ8QACRgADoXSLCEacaxASS9WaLQQ',
        'CAACAgQAAxkBAAEBlMpjtLYIk-y9pdKse5-EYFEZ9ZcDRAACAQYAAtO9YAlUWoU-Mptr-i0E',
        'CAACAgQAAxkBAAEBlM5jtLZKAbIxMx4CuZSe_1sRW_XA6AAC4jQAAuOnXQXilRi6bXq_nS0E',
        'CAACAgIAAxkBAAEBlNJjtLZlTRkIZP0jnfPa2jvBe_vSUQACewADjIhqD4UNiZ3OWJQZLQQ',
        'CAACAgEAAxkBAAEBlNpjtLaWd-95Dws_pLq-P31c4x-4yAACMwIAAhisYEb8n9aiJHmTAAEtBA',
        


    ]

    def execute(self, command):
        self.send_sticker(command, random_element(SendCoffee.stickers))
