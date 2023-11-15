import tkinter as tk

class RecommendationSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Movie Recommendation System")

        self.label_user = tk.Label(self.root, text="Enter User ID:")
        self.entry_user = tk.Entry(self.root)
        self.label_preferences = tk.Label(self.root, text="Enter Movie Preferences (comma-separated):")
        self.entry_preferences = tk.Entry(self.root)
        self.button_recommend = tk.Button(self.root, text="Get Recommendations", command=self.get_recommendations)
        self.text_recommendations = tk.Text(self.root, height=10, width=40)

        self.label_user.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_user.grid(row=0, column=1, padx=5, pady=5)
        self.label_preferences.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_preferences.grid(row=1, column=1, padx=5, pady=5)
        self.button_recommend.grid(row=2, column=0, columnspan=2, pady=10)
        self.text_recommendations.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def get_recommendations(self):
        user_id = self.entry_user.get()
        preferences = self.entry_preferences.get().split(',')

        recommendations = self.content_based_recommendation(preferences)

        self.text_recommendations.delete(1.0, tk.END)
        self.text_recommendations.insert(tk.END, f"Recommended movies for user {user_id}:\n")
        for movie in recommendations:
            self.text_recommendations.insert(tk.END, f"{movie}\n")

    def content_based_recommendation(self, user_preferences):

        movies_data = {
            'Movie1': ['Action', 'Adventure'],
            'Movie2': ['Comedy', 'Romance'],
            'Movie3': ['Action', 'Drama'],
            'Movie4': ['Comedy', 'Adventure'],
            'Movie5': ['Drama', 'Romance'],
        }

        recommendations = []
        for movie, genres in movies_data.items():
            common_genres = set(user_preferences) & set(genres)
            if common_genres:
                recommendations.append(movie)

        return recommendations

    def run(self):
        self.root.mainloop()

recommendation_system_gui = RecommendationSystemGUI()
recommendation_system_gui.run()
