import couchdb


def main():
    try:
        server = couchdb.Server("http://admin:password@localhost:5984/")
        db = server["student"]
        doc = {"type": "person", "name": "Jacqueline Smith", "age": 30}
        
        # add document
        # doc_id, doc_rev = db.save(doc)
        # print('Created document with ID: {0}'.format(doc_id))
        
        # retrive data
        doc_id ="80f80ca81db3bc85b2d9c82428004343"
        
        retrieved_doc = db[doc_id]
        print('Retrieved document: {0}'.format(retrieved_doc))
        
        # Update a field in the document
        retrieved_doc['age'] = 31
        
        # Save the updated document back to the database
        db.save(retrieved_doc)
        print('Updated document: {0}'.format(retrieved_doc))
        
        # Delete the document
        db.delete(retrieved_doc)
        print('Deleted document with ID: {0}'.format(retrieved_doc['_id']))
        

    except Exception as e:
        raise print(e)


if __name__ == "__main__":
    main()
