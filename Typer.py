import functions as fn
data = ""
while True:    
    data += fn.input_data()
    words = fn.count_words(data)
    fn.print_data(data)
