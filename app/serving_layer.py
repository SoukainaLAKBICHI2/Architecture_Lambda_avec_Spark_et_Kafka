import json
import glob

# Lire les résultats batch
batch_files = glob.glob("/app/batch_results/*.json")
batch_data = {}
for file in batch_files:
    with open(file) as f:
        for line in f:
            record = json.loads(line)
            # ignorer les enregistrements vides ou sans total_amount
            if 'customer' in record and 'total_amount' in record:
                batch_data[record['customer']] = batch_data.get(record['customer'], 0) + record['total_amount']

# Simuler des résultats streaming (exemple)
streaming_data = {
    "Ali": 80,
    "Sara": 40,
    "Mounir": 200
}

# Fusion Batch + Streaming
serving_view = {}
for customer in set(batch_data.keys()).union(streaming_data.keys()):
    serving_view[customer] = batch_data.get(customer, 0) + streaming_data.get(customer, 0)

# Sauvegarder la vue finale
with open("/app/serving_view.json", "w") as f:
    json.dump(serving_view, f, indent=4)

print("Serving view:", serving_view)
