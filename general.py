import os

def create_project_directory(directory):
    if not os.path.exists(directory):
        print("creating directory "+ directory )
        os.makedirs(directory)

def create_data_files(project_name , base_url):
    queue=project_name + '/queue.txt'
    crawled = project_name +'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue , base_url)
    if not os.path.isfile(crawled):
        write_file(crawled , '')
        
def write_file(file_path , data):
    file = open(file_path, 'w')
    file.write(data)
    file.close()
    
def append_to_file(file_path , data):
    f = open(file_path , 'a')
    f.write(data + '\n')
    f.close()
    
def delete_content_of_file(file_path, data):
    f=open(file_path , 'w')
    f.close()
    
def file_to_set(file_path):
    links=set()
    f=open(file_path , 'rt')
    for line in f:
        links.add(line.replace('\n' , ''))
    f.close()
    return links

def set_to_file(links , file_path):
    f=open(file_path,'w')
    for link in sorted(links):
        append_to_file(file_path , link)
        

