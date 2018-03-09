# Hashem Selim
#SSW 567
#Description:
#This application will consume a GitHub username in the form of user input.
#It will then return a list of the user's GitHub repos as well as the number of commits.

#Dependencies
import requests
import json


#HTTP GET request on Gitgub RESTful API to receive list of repos.
def repositoryGET(user):
    response = requests.get('https://api.github.com/users/' + user +'/repos')
    apiRepositoryOutput = json.loads(response.text)
    
    repositoryList = []
    for repository in apiRepositoryOutput:
        repositoryList += [repository.get('name')]
    return repositoryList

#HTTP GET request on Gitgub RESTful API to receive number of commits per repo.
def commitsGET(user, repository):
    numcommits = requests.get('https://api.github.com/repos/' +user+'/' + repository + '/commits')
    apiCommitsOutput = json.loads(numcommits.text)
    return len(apiCommitsOutput)

if __name__ == "__main__":
    user = raw_input("GitHub Username: ")
    print("User: " + user)

    repositoryList = repositoryGET(user)

    for index, repository in enumerate(repositoryList):
        print("Repoisory " + str(index))
        print(repository)
        print("Commits: " + str(commitsGET(user,repository)))
        print("")