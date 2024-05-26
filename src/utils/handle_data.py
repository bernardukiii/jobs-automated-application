import pickle, os

class HandleData:
    # Initializer #
    def __init__(self, file_name):
        self.file_name = file_name
        
# First function to check if peexisting information exists
    def check_data(self, user_name):
        filename = user_name.lower()
        file_path = os.path.join(self.data_dir, f'{filename}.pickle')

        if os.path.exists(file_path):
            with open(f'/data/{filename}.pickle', 'rb') as file:
                existing_data = pickle.load(file)
                print('This is your saved information:')
                for field, value in existing_data:
                    print(f"{field}: {value}")
        else:
            print('No preexisting information.')

# Save information
    def save_data(self, data):
        # Check if the data in fact exists
        if data:
            filename = data["name"].lower()
            file_path = os.path.join(self.data_dir, f'{filename}.pickle')

            with open(file_path, 'wb') as file:
                pickle.dump(data, file)
        else:
            print('No information provided.')