
import tkinter as tk
from tkinter import messagebox, simpledialog
from pathlib import Path
from PIL import Image, ImageTk

# Application theme
NAVY = "#081426"
PANEL = "#101F38"
BLUE = "#2563EB"
CYAN = "#06B6D4"
WHITE = "#FFFFFF"
MUTED = "#A9BBD3"
GREEN = "#22C55E"
RED = "#EF4444"


class SmartEducationApp:

    def __init__(self, root):

        self.base_dir = Path(__file__).resolve().parent
        self.root = root

        self.root.title("Smart Education")
        self.root.geometry("1100x700")
        self.root.minsize(800, 550)
        self.root.configure(bg=NAVY)

        self.room_id = None
        self.muted = False
        self.video_on = True

        self.original_bg = None
        self.bg_photo = None

        self.create_interface()

    # Background image
    def resize_background(self, event):

        if self.original_bg is None:
            return

        width = event.width
        height = event.height

        if width < 1 or height < 1:
            return

        image = self.original_bg.resize(
            (width, height),
            Image.Resampling.LANCZOS
        )

        self.bg_photo = ImageTk.PhotoImage(image)
        self.bg_label.config(image=self.bg_photo)

    # Button styling
    def make_button(self, parent, text, command,
                    color, hover_color):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=WHITE,
            activebackground=hover_color,
            activeforeground=WHITE,
            font=("Arial", 12, "bold"),
            relief="flat",
            bd=0,
            padx=22,
            pady=13,
            cursor="hand2"
        )

        button.bind(
            "<Enter>",
            lambda event: button.config(bg=hover_color)
        )

        button.bind(
            "<Leave>",
            lambda event: button.config(bg=color)
        )

        return button

    # Main interface
    def create_interface(self):

        # Header
        header = tk.Frame(
            self.root,
            bg=NAVY,
            height=95
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="SMART EDUCATION",
            font=("Arial", 23, "bold"),
            bg=NAVY,
            fg=WHITE
        )
        title.pack(pady=(15, 3))

        subtitle = tk.Label(
            header,
            text="CONNECT  •  LEARN  •  GROW",
            font=("Arial", 10, "bold"),
            bg=NAVY,
            fg=CYAN
        )
        subtitle.pack()

        # Main background frame
        self.main_frame = tk.Frame(
            self.root,
            bg=NAVY
        )
        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=(5, 22)
        )

        # Load Naruto background
        image_path = self.base_dir / "assets" / "big3.jpg"

        self.original_bg = Image.open(image_path).convert("RGB")

        self.bg_label = tk.Label(
            self.main_frame,
            bg=NAVY
        )

        self.bg_label.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        self.main_frame.bind(
            "<Configure>",
            self.resize_background
        )

        # Central content panel
        card = tk.Frame(
            self.main_frame,
            bg=PANEL,
            padx=45,
            pady=35,
            highlightbackground=CYAN,
            highlightthickness=1
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Welcome heading
        welcome = tk.Label(
            card,
            text="Welcome to Your Learning Room",
            font=("Arial", 22, "bold"),
            bg=PANEL,
            fg=WHITE
        )
        welcome.pack(pady=(5, 8))

        description = tk.Label(
            card,
            text="Your space to connect and learn together",
            font=("Arial", 11),
            bg=PANEL,
            fg=MUTED
        )
        description.pack(pady=(0, 28))

        # Meeting buttons
        meeting_frame = tk.Frame(
            card,
            bg=PANEL
        )
        meeting_frame.pack(pady=5)

        self.make_button(
            meeting_frame,
            " +  Create Meeting",
            self.new_meeting,
            BLUE,
            "#1D4ED8"
        ).grid(row=0, column=0, padx=8)

        self.make_button(
            meeting_frame,
            "Join Meeting",
            self.join_meeting,
            CYAN,
            "#0891B2"
        ).grid(row=0, column=1, padx=8)

        # Meeting status
        status_frame = tk.Frame(
            card,
            bg="#172B49",
            padx=20,
            pady=15
        )
        status_frame.pack(fill="x", pady=25)

        self.room_label = tk.Label(
            status_frame,
            text="●  No active meeting",
            font=("Arial", 12, "bold"),
            bg="#172B49",
            fg=MUTED
        )
        self.room_label.pack()

        # Divider
        tk.Frame(
            card,
            bg="#30415C",
            height=1
        ).pack(fill="x", pady=5)

        # Meeting controls heading
        controls_title = tk.Label(
            card,
            text="MEETING CONTROLS",
            font=("Arial", 10, "bold"),
            bg=PANEL,
            fg=CYAN
        )
        controls_title.pack(pady=(15, 12))

        # Microphone and camera
        controls_frame = tk.Frame(
            card,
            bg=PANEL
        )
        controls_frame.pack()

        self.mute_button = self.make_button(
            controls_frame,
            "🎤  Mute Microphone",
            self.toggle_mute,
            "#253B59",
            "#345477"
        )

        self.mute_button.grid(
            row=0, column=0, padx=8
        )

        self.video_button = self.make_button(
            controls_frame,
            "📹  Stop Video",
            self.toggle_video,
            "#253B59",
            "#345477"
        )

        self.video_button.grid(
            row=0, column=1, padx=8
        )

        # Footer
        footer = tk.Label(
            card,
            text="SMART EDUCATION  •  LEARN WITHOUT LIMITS",
            font=("Arial", 8, "bold"),
            bg=PANEL,
            fg="#7186A5"
        )
        footer.pack(pady=(25, 0))

    # Create meeting
    def new_meeting(self):

        self.room_id = "ABC123"

        self.room_label.config(
            text="●  Meeting ID: " + self.room_id,
            fg=GREEN
        )

        messagebox.showinfo(
            "Meeting Created",
            "Your meeting has been created!\n\nMeeting ID: "
            + self.room_id
        )

    # Join meeting
    def join_meeting(self):

        meeting_id = simpledialog.askstring(
            "Join Meeting",
            "Enter Meeting ID:"
        )

        if meeting_id and meeting_id.strip():

            self.room_id = meeting_id.strip()

            self.room_label.config(
                text="●  Joined Meeting: " + self.room_id,
                fg=GREEN
            )

    # Microphone control
    def toggle_mute(self):

        self.muted = not self.muted

        if self.muted:

            self.mute_button.config(
                text="🔇  Unmute Microphone"
            )

        else:

            self.mute_button.config(
                text="🎤  Mute Microphone"
            )

    # Camera control
    def toggle_video(self):

        self.video_on = not self.video_on

        if self.video_on:

            self.video_button.config(
                text="📹  Stop Video"
            )

        else:

            self.video_button.config(
                text="📷  Start Video"
            )
