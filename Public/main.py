import json


def main(context):
    print("Main")
    
    
    while context["loopCount"]>0:
        # ECS boilerplate code
        
        # Update systems
        # Process entities
        # Handle events

        PreLoop(context = context ) # Pre-loop code

        UpdateSystems(context= context) # Update systems
        PostLoop(context= context) # Post-loop code
        print("Loop: ", context["loopCount"])

        pass
    print("Loop limit reached")

def PreLoop(context):
    print("PreLoop")
    pass
def PostLoop(context):
    print("PostLoop")
    pass
# Update systems takes a variable context

def UpdateSystems(context):
    
    print("UpdateSystems")
    pass
def HandleEvents(context):
    print("HandleEvents")
    pass

def CreateEntities(context):
    print("CreateEntities")
    pass


def loadjson(path:str):
    # Load json file
    data = None
    with open(path, 'r') as f:
        data = json.load(f)
        print("   data is : ", data)  # Debug print
    pass
    return data

if __name__ == "__main__":
    context = {
        "loopCount": 10000,
        "entities": [],
        "components": [],
        "systems": []
    }
    main(context)