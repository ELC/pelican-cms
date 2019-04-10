from invoke import task

@task
def testDocs(c):
    c.run("pipenv run build_docs")
    c.run("pipenv run serve_docs")