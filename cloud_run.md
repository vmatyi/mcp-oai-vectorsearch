# Cloud Run deployment commands

```
cloudshell:~ (project-id)$ gcloud services enable run.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com
cloudshell:~ (project-id)$ gcloud config set run/region europe-central2
cloudshell:~ (project-id)$ gcloud secrets create OPENAI_API_KEY --replication-policy=automatic
cloudshell:~ (project-id)$ echo -n "sk-...api key..." | gcloud secrets versions add OPENAI_API_KEY --data-file=-
cloudshell:~ (project-id)$ gcloud secrets create SESSION_SECRET --replication-policy=automatic
cloudshell:~ (project-id)$ echo -n "...Auth token..." | gcloud secrets versions add SESSION_SECRET --data-file=-
cloudshell:~ (project-id)$ gcloud secrets create VECTOR_STORE_ID --replication-policy=automatic
cloudshell:~ (project-id)$ echo -n "vs_...vector store id..." | gcloud secrets versions add VECTOR_STORE_ID --data-file=-
cloudshell:~ (project-id)$ git clone https://github.com/vmatyi/mcp-oai-vectorsearch
cloudshell:~ (project-id)$ cd mcp-oai-vectorsearch/
```

// cloudshell:~/mcp-oai-vectorsearch (project-id)$ echo "web: python main.py" >>Procfile
// cloudshell:~/mcp-oai-vectorsearch (project-id)$ echo "fastmcp==2.*" >> requirements.txt
// cloudshell:~/mcp-oai-vectorsearch (project-id)$ echo "openai>=1.40,<2" >>requirements.txt

```
cloudshell:~/mcp-oai-vectorsearch (project-id)$ PROJECT_ID=$(gcloud config get-value project)
PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')
SA_EMAIL="$PROJECT_NUMBER-compute@developer.gserviceaccount.com"
echo $SA_EMAIL
cloudshell:~/mcp-oai-vectorsearch (project-id)$ gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:${SA_EMAIL}" \
  --role="roles/secretmanager.secretAccessor"
cloudshell:~/mcp-oai-vectorsearch (project-id)$ gcloud run deploy mcp-oai-vectorsearch \
  --source . \
  --allow-unauthenticated \
  --update-secrets=OPENAI_API_KEY=OPENAI_API_KEY:latest,SESSION_SECRET=SESSION_SECRET:latest,VECTOR_STORE_ID=VECTOR_STORE_ID:latest
```

```
cloudshell:~/mcp-oai-vectorsearch (project-id)$ gcloud run deploy mcp-oai-vectorsearch --source . --allow-unauthenticated
```
