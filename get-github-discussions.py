import requests
import json

# Define the GitHub repository owner and name
owner = "ggerganov"
repo = "llama.cpp"
url = "https://api.github.com/graphql"

# GitHub API token
headers = {
    "Authorization": "ISSA SECRET",
    "Content-Type": "application/json"
}

# GraphQL query to fetch discussions with pagination
query = """
{
  repository(owner: "%s", name: "%s") {
    discussions(first: 100, after: AFTER_CURSOR) {
      pageInfo {
        endCursor
        hasNextPage
      }
      nodes {
        title
        bodyText
        url
        createdAt
        author {
          login
        }
      }
    }
  }
}
""" % (owner, repo)

# Function to get discussions from the repository
def get_discussions():
    discussions = []
    cursor = None
    while True:
        query_with_cursor = query.replace("AFTER_CURSOR", f'"{cursor}"' if cursor else "null")
        response = requests.post(url, headers=headers, json={'query': query_with_cursor})
        if response.status_code == 200:
            result = response.json()
            nodes = result["data"]["repository"]["discussions"]["nodes"]
            discussions.extend(nodes)
            page_info = result["data"]["repository"]["discussions"]["pageInfo"]
            if page_info["hasNextPage"]:
                cursor = page_info["endCursor"]
            else:
                break
        else:
            raise Exception(f"Query failed with status code {response.status_code}: {response.text}")
    return discussions

# Fetch the discussions
try:
    discussions = get_discussions()

    # Format discussions into a JSON
    discussions_json = json.dumps(discussions, indent=4)

    # Save discussions to a JSON file
    with open("discussions.json", "w") as file:
        file.write(discussions_json)

    print("Discussions have been saved to discussions.json")
except Exception as e:
    print(e)
