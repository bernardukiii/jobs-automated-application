import pickle, os

class HandleData:
    # Initializer #
    data_dir = 'src/data'

    def __init__(self):
        # Ensure the data directory exists
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        
# First function to check if peexisting information exists
    def check_data(self, user_name):
        filename = user_name.lower()
        file_path = os.path.join(self.data_dir, f'{filename}.pickle')

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                existing_data = pickle.load(file)
                print('This is your saved information:')
                for field, value in existing_data.items():
                    print(f"{field}: {value}")
                return existing_data
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
                print("Data saved.")
        else:
            print('No information provided.')