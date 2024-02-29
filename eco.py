from datasurface.md.Governance import Ecosystem
from datasurface.md.GitOps import GitHubRepository


def createEcosystem() -> Ecosystem:
    return Ecosystem("Test", GitHubRepository("billynewport/datasurfacetemplate", "main")
                     )
