import os

import uvicorn

if __name__ == '__main__':
    # run server on localhost:8000 with auto-reload
    uvicorn.run("src.main:app",
                host=os.getenv("HOST", "0.0.0.0"),
                port=int(os.getenv("PORT", 8000)),
                reload=True)
