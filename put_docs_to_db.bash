for file in dataset/*; do 
    if [ -f "$file" ]; then 
      echo "$file" 
      mongoimport -d mobile_search -c docs --file $file
    fi 
done