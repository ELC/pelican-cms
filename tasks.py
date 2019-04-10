from invoke import task

@task
def testDocs(c):
    c.run("pipenv run build_docs")
    c.run("pipenv run serve_docs")

@task
def build(c):
    c.run("pipenv run build_web")
    c.run("pipenv run build_desktop")
    