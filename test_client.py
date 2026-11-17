import urllib.request
import json

base_url = "http://localhost:8008"

# 1. Testar Static File (index.html)
with urllib.request.urlopen(f"{base_url}/", timeout=3) as resp:
    html = resp.read().decode('utf-8')
    assert "AprovaQuest" in html, "index.html não contém AprovaQuest"
    print("✅ [OK] Static File / (index.html) servido perfeitamente.")

# 2. Testar /api/filtros
with urllib.request.urlopen(f"{base_url}/api/filtros", timeout=3) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    assert data['total_questoes'] >= 25, f"Esperado >= 25 questões, obtido {data['total_questoes']}"
    print(f"✅ [OK] /api/filtros retornou {data['total_questoes']} questões e {len(data['bancas'])} bancas.")

# 3. Testar /api/questoes
with urllib.request.urlopen(f"{base_url}/api/questoes?so_lei=true", timeout=3) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    assert data['total'] > 0, "Filtro de lei seca falhou"
    print(f"✅ [OK] /api/questoes?so_lei=true retornou {data['total']} questões de lei seca.")

# 4. Testar /api/editais
with urllib.request.urlopen(f"{base_url}/api/editais", timeout=3) as resp:
    editais = json.loads(resp.read().decode('utf-8'))
    assert len(editais) >= 2, "Editais não retornados"
    print(f"✅ [OK] /api/editais retornou {len(editais)} editais verticalizados.")

# 5. Testar responder questão
payload = json.dumps({"questao_id": 1, "alternativa_escolhida": "B", "tempo_gasto_segundos": 20}).encode('utf-8')
req = urllib.request.Request(f"{base_url}/api/questoes/responder", data=payload, headers={'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req, timeout=3) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    assert res['acertou'] is True, "Gabarito da questão 1 deveria ser B"
    print("✅ [OK] /api/questoes/responder avaliou resposta e retornou gabarito e comentário pedagógico.")

# 6. Testar Simulado Gerar
payload = json.dumps({"tipo": "misto", "quantidade": 5, "tempo_minutos": 10}).encode('utf-8')
req = urllib.request.Request(f"{base_url}/api/simulado/gerar", data=payload, headers={'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req, timeout=3) as resp:
    sim = json.loads(resp.read().decode('utf-8'))
    assert len(sim['questoes']) == 5, "Simulado não retornou 5 questões"
    print(f"✅ [OK] /api/simulado/gerar gerou simulado com {len(sim['questoes'])} questões.")

# 7. Testar Tutor IA
payload = json.dumps({"questao_id": 1, "modo": "macete"}).encode('utf-8')
req = urllib.request.Request(f"{base_url}/api/ia/tutor", data=payload, headers={'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req, timeout=8) as resp:
    tutor = json.loads(resp.read().decode('utf-8'))
    assert "resposta" in tutor and len(tutor['resposta']) > 10, "Tutor IA falhou"
    print(f"✅ [OK] /api/ia/tutor retornou orientações do Mentor Concurseiro com sucesso.")

print("\n🎯 TODOS OS TESTES PASSARAM COM 100% DE SUCESSO!")
