#  Avatar Conversationnel Intelligent

Projet d'avatar conversationnel interactif basé sur :
- NLP heuristique
- LLM (Llama 3 via Ollama)
- fusion des analyses
- mémoire conversationnelle enrichie
- avatar animé en Canvas (JavaScript)

---

# Objectif

Créer un avatar capable de :
- comprendre l’émotion d’un utilisateur
- adapter sa réponse et son comportement
- maintenir une mémoire conversationnelle
- simuler une interaction humaine naturelle

---

#  Architecture

## 1. NLP heuristique
- détection de mots-clés
- estimation rapide de l’émotion
- détection des intentions

## 2. Analyse LLM
- compréhension sémantique avancée
- extraction émotion / politesse / urgence

## 3. Fusion
- combinaison NLP + LLM
- résolution des conflits
- génération d’un état émotionnel final

## 4. Génération de réponse
- LLM génère une réponse naturelle
- adaptation du ton selon émotion
- sortie JSON structurée

---

#  Pipeline

Utilisateur  
→ NLP + LLM  
→ Fusion  
→ État émotionnel final  
→ Avatar + mémoire  
→ Réponse LLM  
→ Interface Web

---

#  API

## POST `/chat`

### Request
```json
{
  "message": "Je suis triste"
}
```

---

### Response
```json
{
  "response": "Je suis là pour toi.",
  "avatar": {
    "expression": "triste",
    "gesture": "reconfort",
    "tone": "doux"
  },
  "analysis": {
    "emotion": "sad",
    "speech_act": ["expressive"],
    "politeness": "neutral",
    "urgency": "low"
  }
}
```

---

#  Système d’avatar

## Expressions
- neutre
- triste
- souriant
- calme
- empathique
- concentré

## Gestes
- attente
- ouverture
- apaisement
- réconfort
- rapide

## Ton
- neutre
- doux
- calme
- direct
- chaleureux

---

#  Fusion NLP + LLM

## Stratégie
- accord → émotion conservée
- conflit → priorité LLM
- neutralité → fallback heuristique

## Résultat
Un état émotionnel plus stable et cohérent.

---

#  Mémoire

## Stockage
- messages utilisateur
- réponses avatar
- analyses émotionnelles
- timestamp

## Utilisation
- suivi émotionnel
- continuité conversationnelle
- contexte enrichi pour le LLM

---

#  Installation

## 1. Dépendances

pip install fastapi uvicorn requests

## 2. Lancer Ollama

ollama run llama3.2:3b

## 3. Lancer le backend

uvicorn main:app --reload

## 4. Frontend

Ouvrir frontend/index.html dans un navigateur

---

#  Structure du projet

project/
│
├── main.py
├── nlp_analyzer.py
├── llm_analyzer.py
├── analysis_fusion.py
├── response_generator.py
├── conversation_memory.py
├── avatar_behavior.py
├── run_all.py
│
├── frontend/
│   └── avatar
│   │   └── fichier vtuber
│   ├── index.html
│   ├── script.js
│   └── style.css

---

#  Exemple

Request:
{
  "message": "J’ai peur"
}

Response:
{
  "response": "Je suis là pour toi.",
  "avatar": {
    "expression": "triste",
    "gesture": "reconfort",
    "tone": "doux"
  },
  "analysis": {
    "emotion": "sad",
    "speech_act": ["expressive"],
    "politeness": "neutral",
    "urgency": "low"
  }
}

---

#  Points forts
- architecture modulaire
- fusion NLP + LLM
- mémoire conversationnelle
- avatar Canvas interactif
- analyse émotionnelle dynamique

---

#  Améliorations possibles
- mémoire long terme utilisateur
- scoring émotionnel global
- avatar 2D avancé
- personnalisation utilisateur
- multi-utilisateurs
- résumé automatique des conversations

---

# Auteur
Projet réalisé dans le cadre d’un stage en informatique  
Licence Informatique – 3ème année

---

#  Note
Ce projet utilise un modèle LLM local (Ollama). Aucune donnée n’est envoyée vers un service cloud externe.
