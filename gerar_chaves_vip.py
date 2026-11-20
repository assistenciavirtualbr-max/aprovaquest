#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Chaves de Ativação VIP - AprovaQuest
Gere chaves individuais para seus compradores (Kiwify, Hotmart, Mercado Pago, WhatsApp).
"""

import random
import string
import datetime

def gerar_chave_vip(prefixo="APROVA"):
    chars = string.ascii_uppercase + string.digits
    parte1 = ''.join(random.choices(chars, k=4))
    parte2 = ''.join(random.choices(chars, k=4))
    return f"{prefixo}-{parte1}-{parte2}"

def gerar_lote(quantidade=10):
    print("=" * 60)
    print(f"🔑 LOTE DE {quantidade} CHAVES VIP GERADAS COM SUCESSO - APROVAQUEST")
    print(f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 60)
    chaves = []
    for i in range(1, quantidade + 1):
        chave = gerar_chave_vip()
        chaves.append(chave)
        print(f"[{i:02d}] {chave}")
    print("=" * 60)
    print("💡 Como usar: Envie uma chave dessas para o cliente após a compra.")
    print("O cliente digita a chave no app e tem liberação vitalícia imediata!")
    print("=" * 60)
    return chaves

if __name__ == '__main__':
    import sys
    qtd = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    gerar_lote(qtd)
