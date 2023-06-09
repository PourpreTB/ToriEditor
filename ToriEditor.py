# Développé avec ❤️ par Pourpre - Discord: mk.#7778
# Profitez bien du script ! N'hésitez pas à me contacter si vous avez des questions.


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QComboBox
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
import sys, os

class MainWindow(QMainWindow):
    def __init__(self):
        global color_id
        super().__init__()

        self.setWindowTitle("Tori Editor | made by Pourpre")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(450, 300)

        dropdown_values = ["Default (0)", "Acid (26)", "Adamantium (75)", "Alphaimperial (110)", "Amber (61)", "Amethyst (27)", "Aqua (28)", "Astro (131)", "Aurora (22)", "Azurite (62)", "Beetle (92)", "Blossom (53)", "Boreal (51)", "Bronze (29)", "Camo (101)", "Chronos (42)", "Cobra (89)", "Copper (16)", "Crimson (57)", "Crusher (129)", "Demolition (113)", "Demon (30)", "Diamond (136)", "Dragon (31)", "Ecto (12)", "Elf (32)", "Fossil (134)", "Gaia (43)", "Gladiator (44)", "Gold (33)", "Hawk (55)", "Helios (123)", "Hotpink (105)", "Hunter (95)", "Hydra (45)", "Imperial (86)", "Impure (125)", "Ivory (97)", "Ivy (137)", "Juryo (21)", "Kevlar (108)", "Knox (121)", "Magma (128)", "Magnetite (102)", "Mana (133)", "Marine (34)", "Maya (109)", "Meteor (135)", "Mysterio (118)", "Neptune (11)", "Noxious (35)", "Oldgold (100)", "Olive (124)", "Onyx (69)", "Orc (36)", "Persia (114)", "Pharos (46)", "Plasma (59)", "Platinum (87)", "Pure (50)", "Quicksilver (37)", "Radioactive (38)", "Raider (106)", "Raptor (58)", "Ruby (70)", "Sakura (132)", "Sapphire (39)", "Shaman (65)", "Sphinx (47)", "Spring (10)", "Static (9)", "Superfly (120)", "Superior (130)", "Supernova (71)", "Tesla (54)", "Titan (48)", "Toxic (40)", "Typhon (49)", "Tyrian (107)", "Vampire (41)", "Velvet (115)", "Viridian (64)", "Void (85)", "Vortex (4)", "Vulcan (104)", "Warrior (116)", "Wildfire (52)"]
        combo_box = QComboBox()

        color_id = {
            "Default (0)": 0,
            "Acid (26)" : 26,
            "Adamantium (75)" : 75,
            "Alphaimperial (110)" : 110,
            "Amber (61)" : 61,
            "Amethyst (27)" : 27,
            "Aqua (28)" : 28,
            "Astro (131)" : 131,
            "Aurora (22)" : 22,
            "Azurite (62)" : 62,
            "Beetle (92)" : 92,
            "Blossom (53)" : 53,
            "Boreal (51)" : 51,
            "Bronze (29)" : 29,
            "Camo (101)" : 101,
            "Chronos (42)" : 42,
            "Cobra (89)" : 89,
            "Copper (16)" : 16,
            "Crimson (57)" : 57,
            "Crusher (129)" : 129,
            "Demolition (113)" : 113,
            "Demon (30)" : 30,
            "Diamond (136)" : 136,
            "Dragon (31)" : 31,
            "Ecto (12)" : 12,
            "Elf (32)" : 32,
            "Fossil (134)" : 134,
            "Gaia (43)" : 43,
            "Gladiator (44)" : 44,
            "Gold (33)" : 33,
            "Hawk (55)" : 55,
            "Helios (123)" : 123,
            "Hotpink (105)" : 105,
            "Hunter (95)" : 95,
            "Hydra (45)" : 45,
            "Imperial (86)" : 86,
            "Impure (125)" : 125,
            "Ivory (97)" : 97,
            "Ivy (137)" : 137,
            "Juryo (21)" : 21,
            "Kevlar (108)" : 108,
            "Knox (121)" : 121,
            "Magma (128)" : 128,
            "Magnetite (102)" : 102,
            "Mana (133)" : 133,
            "Marine (34)" : 34,
            "Maya (109)" : 109,
            "Meteor (135)" : 135,
            "Mysterio (118)" : 118,
            "Neptune (11)" : 11,
            "Noxious (35)" : 35,
            "Oldgold (100)" : 100,
            "Olive (124)" : 124,
            "Onyx (69)" : 69,
            "Orc (36)" : 36,
            "Persia (114)" : 114,
            "Pharos (46)" : 46,
            "Plasma (59)" : 59,
            "Platinum (87)" : 87,
            "Pure (50)" : 50,
            "Quicksilver (37)" : 37,
            "Radioactive (38)" : 38,
            "Raider (106)" : 106,
            "Raptor (58)" : 58,
            "Ruby (70)" : 70,
            "Sakura (132)" : 132,
            "Sapphire (39)" : 39,
            "Shaman (65)" : 65,
            "Sphinx (47)" : 47,
            "Spring (10)" : 10,
            "Static (9)" : 9,
            "Superfly (120)" : 120,
            "Superior (130)" : 130,
            "Supernova (71)" : 71,
            "Tesla (54)" : 54,
            "Titan (48)" : 48,
            "Toxic (40)" : 40,
            "Typhon (49)" : 49,
            "Tyrian (107)" : 107,
            "Vampire (41)" : 41,
            "Velvet (115)" : 115,
            "Viridian (64)" : 64,
            "Void (85)" : 85,
            "Vortex (4)" : 4,
            "Warrior (116)" : 116,
            "Wildfire (52)" : 52}

        label_file = QLabel("File Path:")
        self.text_file = QLineEdit()
        button_file = QPushButton("Select File Path")
        button_file.clicked.connect(self.select_file)
        layout_file = QHBoxLayout()
        layout_file.addWidget(label_file)
        layout_file.addWidget(self.text_file)
        layout_file.addWidget(button_file)

        label_force_color = QLabel("Force Color:")
        self.dropdown_force_color = QComboBox()
        self.dropdown_force_color.addItems(dropdown_values)
        layout_force_color = QHBoxLayout()
        layout_force_color.addWidget(label_force_color)
        layout_force_color.addWidget(self.dropdown_force_color)

        button_force_edit = QPushButton("Edit Force Color")
        button_force_edit.clicked.connect(self.modify_force_color)
        layout_force_color.addWidget(button_force_edit)

        label_relax_color = QLabel("Relax Color:")
        self.dropdown_relax_color = QComboBox()
        self.dropdown_relax_color.addItems(dropdown_values)
        layout_relax_color = QHBoxLayout()
        layout_relax_color.addWidget(label_relax_color)
        layout_relax_color.addWidget(self.dropdown_relax_color)
        

        button_relax_edit = QPushButton("Edit Relax Color")
        button_relax_edit.clicked.connect(self.modify_relax_color)
        layout_relax_color.addWidget(button_relax_edit)

        label_torso_color = QLabel("Torso Color:")
        self.dropdown_torso_color = QComboBox()
        self.dropdown_torso_color.addItems(dropdown_values)
        layout_torso_color = QHBoxLayout()
        layout_torso_color.addWidget(label_torso_color)
        layout_torso_color.addWidget(self.dropdown_torso_color)

        button_torso_edit = QPushButton("Edit Torso Color")
        button_torso_edit.clicked.connect(self.modify_torso_color)
        layout_torso_color.addWidget(button_torso_edit)

        label_ghost_color = QLabel("Ghost Color:")
        self.dropdown_ghost_color = QComboBox()
        self.dropdown_ghost_color.addItems(dropdown_values)
        layout_ghost_color = QHBoxLayout()
        layout_ghost_color.addWidget(label_ghost_color)
        layout_ghost_color.addWidget(self.dropdown_ghost_color)


        button_ghost_edit = QPushButton("Edit Ghost Color")
        button_ghost_edit.clicked.connect(self.modify_ghost)
        layout_ghost_color.addWidget(button_ghost_edit)
        
        label_dq_ring_color = QLabel("DQ Ring Color:")
        self.dropdown_dq_ring_color = QComboBox()
        self.dropdown_dq_ring_color.addItems(dropdown_values)
        layout_dq_ring_color = QHBoxLayout()
        layout_dq_ring_color.addWidget(label_dq_ring_color)
        layout_dq_ring_color.addWidget(self.dropdown_dq_ring_color)


        button_dq_ring_edit = QPushButton("Edit DQ Ring Color")
        button_dq_ring_edit.clicked.connect(self.modify_dq_ring)
        layout_dq_ring_color.addWidget(button_dq_ring_edit)

        label_timer_color = QLabel("Timer Color:")
        self.dropdown_timer_color = QComboBox()
        self.dropdown_timer_color.addItems(dropdown_values)
        layout_timer_color = QHBoxLayout()
        layout_timer_color.addWidget(label_timer_color)
        layout_timer_color.addWidget(self.dropdown_timer_color)


        button_timer_edit = QPushButton("Edit Timer Color")
        button_timer_edit.clicked.connect(self.modify_timer)
        layout_timer_color.addWidget(button_timer_edit)

        label_emote_color = QLabel("Emote Color:")
        self.dropdown_emote_color = QComboBox()
        self.dropdown_emote_color.addItems(dropdown_values)
        layout_emote_color = QHBoxLayout()
        layout_emote_color.addWidget(label_emote_color)
        layout_emote_color.addWidget(self.dropdown_emote_color)


        button_emote_edit = QPushButton("Edit Emote Color")
        button_emote_edit.clicked.connect(self.modify_emote)
        layout_emote_color.addWidget(button_emote_edit)

        label_grip_color = QLabel("Grip Color:")
        self.dropdown_grip_color = QComboBox()
        self.dropdown_grip_color.addItems(dropdown_values)
        layout_grip_color = QHBoxLayout()
        layout_grip_color.addWidget(label_grip_color)
        layout_grip_color.addWidget(self.dropdown_grip_color)


        button_grip_edit = QPushButton("Edit Grip Color")
        button_grip_edit.clicked.connect(self.modify_grip)
        layout_grip_color.addWidget(button_grip_edit)

        label_gradcol1_color = QLabel("Primary Gradient Color:")
        self.dropdown_gradcol1_color = QComboBox()
        self.dropdown_gradcol1_color.addItems(dropdown_values)
        layout_gradcol1_color = QHBoxLayout()
        layout_gradcol1_color.addWidget(label_gradcol1_color)
        layout_gradcol1_color.addWidget(self.dropdown_gradcol1_color)


        button_gradcol1_edit = QPushButton("Edit Primary Gradient Color")
        button_gradcol1_edit.clicked.connect(self.modify_gradcol1)
        layout_gradcol1_color.addWidget(button_gradcol1_edit)

        label_gradcol2_color = QLabel("Secondary Gradient Color:")
        self.dropdown_gradcol2_color = QComboBox()
        self.dropdown_gradcol2_color.addItems(dropdown_values)
        layout_gradcol2_color = QHBoxLayout()
        layout_gradcol2_color.addWidget(label_gradcol2_color)
        layout_gradcol2_color.addWidget(self.dropdown_gradcol2_color)


        button_gradcol2_edit = QPushButton("Edit Secondary Gradient Color")
        button_gradcol2_edit.clicked.connect(self.modify_gradcol2)
        layout_gradcol2_color.addWidget(button_gradcol2_edit)

        layout = QVBoxLayout()
        layout.addLayout(layout_file)
        layout.addLayout(layout_force_color)
        layout.addLayout(layout_relax_color)
        layout.addLayout(layout_torso_color)
        layout.addLayout(layout_ghost_color)
        layout.addLayout(layout_dq_ring_color)
        layout.addLayout(layout_timer_color)
        layout.addLayout(layout_emote_color)
        layout.addLayout(layout_grip_color)
        layout.addLayout(layout_gradcol1_color)
        layout.addLayout(layout_gradcol2_color)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            self.text_file.setText(file_path)

    def modify_force_color(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_force_color.currentText()
        print(color)
        for i in color_id:
            print(i)

        if color in color_id:
            color_code = color_id[color]
        else:
            print("problème")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        words = lines[6].split()
        words[2::2] = [str(color_code)] * 21
        words[-1] = '0'
        lines[6] = ' '.join(words) + '\n'

        words = lines[8].split()
        words[2::2] = [str(color_code)] * 21
        words[-1] = '0'
        lines[8] = ' '.join(words) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Force color edited successfully!")

    def modify_relax_color(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")        

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_relax_color.currentText()

        if color in color_id:
            color_code = color_id[color]
        print(color)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        words = lines[7].split()
        words[2::2] = [str(color_code)] * 21
        words[-1] = '0'
        lines[7] = ' '.join(words) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Relax color edited successfully!")

    def modify_torso_color(self):
        initial_string = "BODCOL 0;0 x 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 x 12 x 13 x 14 x 15 x 16 x 17 x 18 x 19 x 20 x\n"
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_torso_color.currentText()
        if color in color_id:
            color_code = color_id[color]    
        with open(file_path, "r") as file:    
            lines = file.readlines()

        user_values = [color_code, color_code, color_code, color_code]

        with open(file_path, "r") as file:
            lines = file.readlines()

        user_value_index = 0
        final_string = ""
        x_counter = 0

        for character in initial_string:
            if character == "x":
                if x_counter in [1, 2, 5, 8]:
                    final_string += str(user_values[user_value_index])
                    user_value_index += 1
                else:
                    final_string += character
                x_counter += 1
            else:
                final_string += character

        simplified_final_string = final_string.replace('x', '0')

        lines[3] = simplified_final_string

        with open(file_path, "w") as file:
            file.writelines(lines)
        
        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")
        
        QMessageBox.information(self, "Success", "Torso color edited successfully!")

    def modify_ghost(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_ghost_color.currentText()
        if color in color_id:
            color_code = color_id[color]    
        with open(file_path, "r") as file:    
            lines = file.readlines()

        
        words = lines[2].split()
        words[6] = str(color_code)
        lines[2] = " ".join(words) + "\n"

        
        with open(file_path, "w") as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Ghost color edited successfully!")


    def modify_dq_ring(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_dq_ring_color.currentText()
        if color in color_id:
            color_code = color_id[color]   
        
        with open(file_path, "r") as file:
            
            lines = file.readlines()

        
        words = lines[2].split()
        words[5] = str(color_code)
        lines[2] = " ".join(words) + "\n"

        
        with open(file_path, "w") as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "DQ Ring edited successfully!")


    def modify_timer(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_timer_color.currentText()
        if color in color_id:
            color_code = color_id[color]   
        
        with open(file_path, "r") as file:
            
            lines = file.readlines()

        
        words = lines[2].split()
        words[8] = str(color_code)
        lines[2] = " ".join(words) + "\n"

        
        with open(file_path, "w") as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Timer color edited successfully!")

    def modify_emote(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_emote_color.currentText()
        if color in color_id:
            color_code = color_id[color]   
        
        with open(file_path, "r") as file:
            
            lines = file.readlines()

        
        words = lines[2].split()
        words[14] = str(color_code)
        lines[2] = " ".join(words) + "\n"

        
        with open(file_path, "w") as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Emote color edited successfully!")

    def modify_grip(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_grip_color.currentText()
        if color in color_id:
            color_code = color_id[color]   
        
        with open(file_path, "r") as file:
            
            lines = file.readlines()

        
        words = lines[2].split()
        words[15] = str(color_code)
        lines[2] = " ".join(words) + "\n"

        
        with open(file_path, "w") as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Grip color edited successfully!")

    def modify_gradcol1(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_gradcol1_color.currentText()
        if color in color_id:
            color_code = color_id[color]   
        with open(file_path, 'r') as file:
            lines = file.readlines()

        words = lines[4].split()
        words[2::2] = [str(color_code)] * 21
        lines[4] = ' '.join(words) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")

        QMessageBox.information(self, "Success", "Primary Gradient edited successfully!")

    def modify_gradcol2(self):
        file_path = self.text_file.text()

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en écriture.")
        else:
            print("Le fichier n'existe pas.")

        if not file_path:
            QMessageBox.warning(self, "Error", "Please select a file.")
            return

        color = self.dropdown_gradcol2_color.currentText()
        if color in color_id:
            color_code = color_id[color]
        with open(file_path, 'r') as file:
            lines = file.readlines()

        words = lines[5].split()
        words[2::2] = [str(color_code)] * 21
        lines[5] = ' '.join(words) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)

        if os.path.exists(file_path):
            permissions = os.stat(file_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(file_path, nouveau_permissions)
            print("Le fichier a été défini en lecture seule.")
        else:
            print("Le fichier n'existe pas.")
        
        QMessageBox.information(self, "Success", "Primary Gradient edited successfully!")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
