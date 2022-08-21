# notes #

/authors method = 'GET','POST' : return all authors, create author

/authors/<id>/ method = 'GET','POST' :  get details of author, update an author

/authors/<id>/ method = 'DELETE' :  delete author

/authors/<authorname>/ method = 'GET','POST','DELETE': Reads, Updates, Deletes authors with given name
example: authors/TarunPatibandla/
         authors/Tarun-Patibandla/ #slugs

/authors/<id>/blogs/ method = 'GET' : get blogs of author
