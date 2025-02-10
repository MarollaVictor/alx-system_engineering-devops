import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    todos = todos_response.json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print ("Employee {} is done with tasks ({}/{})".format(user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
