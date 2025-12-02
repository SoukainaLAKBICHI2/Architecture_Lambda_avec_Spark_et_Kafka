# Atelier Lambda : Spark + Kafka

## 1. Objectifs de l’atelier
- Implémenter un traitement batch avec Spark pour calculer des agrégations sur des données historiques.  
- Implémenter un traitement streaming avec Spark Structured Streaming à partir d’un topic Kafka.  

## 2. Structure du projet

```

atelier-lambda/
├─ docker-compose.yml
├─ app/
│  ├─ datasets/
│  │  └─ transactions.json
│  ├─ batch_job.py
│  ├─ streaming_job.py
│  └─ serving_layer.py
├─ images/

````

## 3. Dataset utilisé

Fichier : `app/datasets/transactions.json`

![dataset](./images/dataset.png)


Ce dataset représente des transactions simples : un client et un montant.

## 4. Mise en place de l’environnement (Docker Compose)

Fichier : `docker-compose.yml`

Pour démarrer les services :

```bash
docker compose up -d
```
![docker](./images/docker-compose.png)

Vérifier que les conteneurs tournent :

```bash
docker ps
```

## 5. Batch Layer – Traitement des données historiques

**Fichier :** `app/batch_job.py`

![batch](./images/batch.png)

**Objectif pédagogique :**

* Comprendre le rôle de la Batch Layer.
* Lire des données historiques et produire une vue agrégée.

**Exécution :**

![batch-exec](./images/batch-exec.png)

## 6. Speed Layer – Traitement en temps réel avec Kafka + Spark Streaming

### 6.1 Création du topic Kafka

![topic](./images/topic1.png)

Vérification :

![verification](images/verification.png)


### 6.2 Producteur Kafka

Pour envoyer des événements en temps réel :

![producer](images/producer.png)

### 6.3 Spark Streaming Job

**Fichier :** `app/streaming_job.py`

![streaming](images/streaming.png)

**Exécution :**

![streaming-exec](images/Sreaming-exec.png)

## 7. Serving Layer – Fusion Batch + Streaming

**Fichier :** `app/serving_layer.py`

![serving](images/serving.png)

Objectif pédagogique :

* Montrer le rôle de la Serving Layer.
* Combiner précision (batch) et réactivité (streaming).

## 8. Resultat

![serving-exec](images/serving_exec.png)
![serving-view](images/serving-view.png)


