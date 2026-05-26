"""
Project LAKSHYA — FastAPI Entry Point
Accepts raw APK upload, routes through the 4-module forensic pipeline.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil, os, uuid

app = FastAPI(title="Project LAKSHYA", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "/tmp/lakshya_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def health():
    return {"status": "LAKSHYA online", "version": "1.0.0"}


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith(".apk"):
        raise HTTPException(status_code=400, detail="Only .apk files accepted.")

    job_id   = str(uuid.uuid4())[:8]
    apk_path = os.path.join(UPLOAD_DIR, f"{job_id}_{file.filename}")

    with open(apk_path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    try:
        from core_parsers.manifest_parser import parse_manifest
        from core_parsers.spoof_detector  import detect_brand_spoof
        from core_parsers.threat_scorer   import compute_threat_score
        from genealogy.fcg_extractor      import extract_fcg
        from genealogy.dna_matcher        import match_dna
        from clustering_engine.ioc_extractor  import extract_iocs
        from clustering_engine.graph_cluster  import build_cluster

        manifest   = parse_manifest(apk_path)
        spoof      = detect_brand_spoof(apk_path)
        score      = compute_threat_score(manifest, spoof)
        fcg        = extract_fcg(apk_path)
        dna        = match_dna(fcg)
        iocs       = extract_iocs(apk_path)
        cluster    = build_cluster(iocs)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(apk_path)

    return {
        "job_id":    job_id,
        "manifest":  manifest,
        "spoof":     spoof,
        "score":     score,
        "dna":       dna,
        "iocs":      iocs,
        "cluster":   cluster,
    }
