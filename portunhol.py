# -*- coding: utf-8 -*-
"""Transforms portuguese in portunhol."""

__author__ = 'Roberto De Almeida <roberto@dealmeida.net>'
__license__ = 'PSF'
__contributors__ = 'Fernando Serboncini'
import os, sys
#import Image
import string
import re

regexps = [
           # palavras
           (r"\beu\b", "jo"),
           (r"\bmas\b", "pero"),
           (r"\buma\b", "una"),
           (r"\bum\b", "uno"),
           (r"\b(minha|meu)\b", "mi"),
           (r"\b(s|t)(ua|eu)\b", r"\1u"),
           (r"\b(tu|você)\b", "usted"),
           (r"\bdo\b", "del"),
           (r"\bem\b", "en"),
           (r"\bomo\b", "bueno"),
           (r"\b(a|o)(s?)\b", r"l\1\2"),
           (r"\bé\b", "es"),
           (r"\bcara\b", "cabrón"),
           (r"\bhoje\b", "hoy"),
           (r"\bisso\b", "esso"),
           (r"\bmuito\b", "mucho"),

           # pedaços
           (r"\b(\w{2,}?)ção\b", r"\1ción"),
           (r"\b(\w{2,}?)ções\b", r"\1ciónes"),
           (r"\b(\w{3,}?)ão\b", r"\1ión"),
           (r"\b(\w{3,}?)ões\b", r"\1iónes"),
           (r"\b(\w*)inh(a|o)\b", r"\1it\2"),
           (r"\b(\w*)al\b", r"\1ale"),
           (r"\b(\w)o(\w{2,3})\b", r"\1ue\2"),
           (r"\b(\w)e(\w{2,3})\b", r"\1ie\2"),
           (r"\b(\w{3,}?)dade\b", r"\1dad"),
           ("nh", u"ñ"),
          ]


def portunholator(input):
    for pattern, repl in regexps:
        p = re.compile(pattern, re.U)
        input = p.sub(repl, input)
    print input
    

if __name__ == '__main__':
    frase_em_portugues = sys.argv[1]
    portunholator(frase_em_portugues)