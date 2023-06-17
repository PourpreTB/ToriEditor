# Developed with ❤️ by Pourpre - Discord: mk.#7778
# Enjoy the script! Don't hesitate to contact me if you have any questions.

from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QMainWindow, QPushButton, QLineEdit, QApplication

import sys, requests, os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QComboBox,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from var import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToriEditor by Pourpre")
        self.setWindowIcon(QIcon('torieditor.ico'))
        self.setGeometry(590, 590, 470, 470)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)


        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBarAutoHide(True)
        self.tab_widget.addTab(self.tab1, "Items")
        self.tab_widget.addTab(self.tab2, "Colors")
        main_layout.addWidget(self.tab_widget)


        self.setup_tab1()
        self.setup_tab2()

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.file_label = QLabel("File Path:")
        self.file_text = QLineEdit()
        self.file_button = QPushButton("Select File Path")
        self.file_button.clicked.connect(self.select_file)

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_text)
        file_layout.addWidget(self.file_button)

        self.apply_button = QPushButton("Apply")
        self.apply_button.setEnabled(False)
        self.apply_button.clicked.connect(self.apply_button_clicked)


        bottom_layout = QVBoxLayout()
        bottom_layout.addLayout(file_layout)
        bottom_layout.addWidget(self.apply_button)

        main_layout.addWidget(self.console)
        main_layout.addLayout(bottom_layout)

        
    def setup_tab1(self):
        main_layout = QVBoxLayout()
        self.tab1.setLayout(main_layout)

        labels_layout = QHBoxLayout()
        main_layout.addLayout(labels_layout)

        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        labels_layout.addLayout(left_layout)
        labels_layout.addLayout(right_layout)

        label_head = QLabel("head:")
        self.combobox_head = QComboBox()
        for key in head.keys():
            head_item_id = head[key]["item_id"]
            self.combobox_head.addItem(
                QIcon(
                    f"images/{head_item_id}.png"
                ),
                key,
            )

        label_layout_head = QHBoxLayout()
        label_layout_head.addWidget(label_head)
        label_layout_head.addWidget(self.combobox_head)
        left_layout.addLayout(label_layout_head)

        label_breast = QLabel("breast:")
        self.combobox_breast = QComboBox()
        for key in breast.keys():
            breast_item_id = breast[key]["item_id"]
            self.combobox_breast.addItem(
                QIcon(
                    f"images/{breast_item_id}.png"
                ),
                key,
            )

        label_layout_breast = QHBoxLayout()
        label_layout_breast.addWidget(label_breast)
        label_layout_breast.addWidget(self.combobox_breast)
        right_layout.addLayout(label_layout_breast)

        label_chest = QLabel("chest:")
        self.combobox_chest = QComboBox()
        for key in chest.keys():
            chest_item_id = chest[key]["item_id"]
            self.combobox_chest.addItem(
                QIcon(
                    f"images/{chest_item_id}.png"
                ),
                key,
            )

        label_layout_chest = QHBoxLayout()
        label_layout_chest.addWidget(label_chest)
        label_layout_chest.addWidget(self.combobox_chest)
        left_layout.addLayout(label_layout_chest)

        label_stomach = QLabel("stomach:")
        self.combobox_stomach = QComboBox()
        for key in stomach.keys():
            stomach_item_id = stomach[key]["item_id"]
            self.combobox_stomach.addItem(
                QIcon(
                    f"images/{stomach_item_id}.png"
                ),
                key,
            )

        label_layout_stomach = QHBoxLayout()
        label_layout_stomach.addWidget(label_stomach)
        label_layout_stomach.addWidget(self.combobox_stomach)
        right_layout.addLayout(label_layout_stomach)

        label_groin = QLabel("groin:")
        self.combobox_groin = QComboBox()
        for key in groin.keys():
            groin_item_id = groin[key]["item_id"]
            self.combobox_groin.addItem(
                QIcon(
                    f"images/{groin_item_id}.png"
                ),
                key,
            )

        label_layout_groin = QHBoxLayout()
        label_layout_groin.addWidget(label_groin)
        label_layout_groin.addWidget(self.combobox_groin)
        left_layout.addLayout(label_layout_groin)

        label_r_pecs = QLabel("r_pecs:")
        self.combobox_r_pecs = QComboBox()
        for key in r_pecs.keys():
            r_pecs_item_id = r_pecs[key]["item_id"]
            self.combobox_r_pecs.addItem(
                QIcon(
                    f"images/{r_pecs_item_id}.png"
                ),
                key,
            )

        label_layout_r_pecs = QHBoxLayout()
        label_layout_r_pecs.addWidget(label_r_pecs)
        label_layout_r_pecs.addWidget(self.combobox_r_pecs)
        right_layout.addLayout(label_layout_r_pecs)

        label_r_biceps = QLabel("r_biceps:")
        self.combobox_r_biceps = QComboBox()
        for key in r_biceps.keys():
            r_biceps_item_id = r_biceps[key]["item_id"]
            self.combobox_r_biceps.addItem(
                QIcon(
                    f"images/{r_biceps_item_id}.png"
                ),
                key,
            )

        label_layout_r_biceps = QHBoxLayout()
        label_layout_r_biceps.addWidget(label_r_biceps)
        label_layout_r_biceps.addWidget(self.combobox_r_biceps)
        left_layout.addLayout(label_layout_r_biceps)

        label_r_triceps = QLabel("r_triceps:")
        self.combobox_r_triceps = QComboBox()
        for key in r_triceps.keys():
            r_triceps_item_id = r_triceps[key]["item_id"]
            self.combobox_r_triceps.addItem(
                QIcon(
                    f"images/{r_triceps_item_id}.png"
                ),
                key,
            )

        label_layout_r_triceps = QHBoxLayout()
        label_layout_r_triceps.addWidget(label_r_triceps)
        label_layout_r_triceps.addWidget(self.combobox_r_triceps)
        right_layout.addLayout(label_layout_r_triceps)

        label_l_pecs = QLabel("l_pecs:")
        self.combobox_l_pecs = QComboBox()
        for key in l_pecs.keys():
            l_pecs_item_id = l_pecs[key]["item_id"]
            self.combobox_l_pecs.addItem(
                QIcon(
                    f"images/{l_pecs_item_id}.png"
                ),
                key,
            )

        label_layout_l_pecs = QHBoxLayout()
        label_layout_l_pecs.addWidget(label_l_pecs)
        label_layout_l_pecs.addWidget(self.combobox_l_pecs)
        left_layout.addLayout(label_layout_l_pecs)

        label_l_biceps = QLabel("l_biceps:")
        self.combobox_l_biceps = QComboBox()
        for key in l_biceps.keys():
            l_biceps_item_id = l_biceps[key]["item_id"]
            self.combobox_l_biceps.addItem(
                QIcon(
                    f"images/{l_biceps_item_id}.png"
                ),
                key,
            )

        label_layout_l_biceps = QHBoxLayout()
        label_layout_l_biceps.addWidget(label_l_biceps)
        label_layout_l_biceps.addWidget(self.combobox_l_biceps)
        right_layout.addLayout(label_layout_l_biceps)

        label_l_triceps = QLabel("l_triceps:")
        self.combobox_l_triceps = QComboBox()
        for key in l_triceps.keys():
            l_triceps_item_id = l_triceps[key]["item_id"]
            self.combobox_l_triceps.addItem(
                QIcon(
                    f"images/{l_triceps_item_id}.png"
                ),
                key,
            )

        label_layout_l_triceps = QHBoxLayout()
        label_layout_l_triceps.addWidget(label_l_triceps)
        label_layout_l_triceps.addWidget(self.combobox_l_triceps)
        left_layout.addLayout(label_layout_l_triceps)

        label_r_hand = QLabel("r_hand:")
        self.combobox_r_hand = QComboBox()
        for key in r_hand.keys():
            r_hand_item_id = r_hand[key]["item_id"]
            self.combobox_r_hand.addItem(
                QIcon(
                    f"images/{r_hand_item_id}.png"
                ),
                key,
            )

        label_layout_r_hand = QHBoxLayout()
        label_layout_r_hand.addWidget(label_r_hand)
        label_layout_r_hand.addWidget(self.combobox_r_hand)
        right_layout.addLayout(label_layout_r_hand)

        label_l_hand = QLabel("l_hand:")
        self.combobox_l_hand = QComboBox()
        for key in l_hand.keys():
            l_hand_item_id = l_hand[key]["item_id"]
            self.combobox_l_hand.addItem(
                QIcon(
                    f"images/{l_hand_item_id}.png"
                ),
                key,
            )

        label_layout_l_hand = QHBoxLayout()
        label_layout_l_hand.addWidget(label_l_hand)
        label_layout_l_hand.addWidget(self.combobox_l_hand)
        left_layout.addLayout(label_layout_l_hand)

        label_r_butt = QLabel("r_butt:")
        self.combobox_r_butt = QComboBox()
        for key in r_butt.keys():
            r_butt_item_id = r_butt[key]["item_id"]
            self.combobox_r_butt.addItem(
                QIcon(
                    f"images/{r_butt_item_id}.png"
                ),
                key,
            )

        label_layout_r_butt = QHBoxLayout()
        label_layout_r_butt.addWidget(label_r_butt)
        label_layout_r_butt.addWidget(self.combobox_r_butt)
        right_layout.addLayout(label_layout_r_butt)

        label_l_butt = QLabel("l_butt:")
        self.combobox_l_butt = QComboBox()
        for key in l_butt.keys():
            l_butt_item_id = l_butt[key]["item_id"]
            self.combobox_l_butt.addItem(
                QIcon(
                    f"images/{l_butt_item_id}.png"
                ),
                key,
            )

        label_layout_l_butt = QHBoxLayout()
        label_layout_l_butt.addWidget(label_l_butt)
        label_layout_l_butt.addWidget(self.combobox_l_butt)
        left_layout.addLayout(label_layout_l_butt)

        label_r_thigh = QLabel("r_thigh:")
        self.combobox_r_thigh = QComboBox()
        for key in r_thigh.keys():
            r_thigh_item_id = r_thigh[key]["item_id"]
            self.combobox_r_thigh.addItem(
                QIcon(
                    f"images/{r_thigh_item_id}.png"
                ),
                key,
            )

        label_layout_r_thigh = QHBoxLayout()
        label_layout_r_thigh.addWidget(label_r_thigh)
        label_layout_r_thigh.addWidget(self.combobox_r_thigh)
        right_layout.addLayout(label_layout_r_thigh)

        label_l_thigh = QLabel("l_thigh:")
        self.combobox_l_thigh = QComboBox()
        for key in l_thigh.keys():
            l_thigh_item_id = l_thigh[key]["item_id"]
            self.combobox_l_thigh.addItem(
                QIcon(
                    f"images/{l_thigh_item_id}.png"
                ),
                key,
            )

        label_layout_l_thigh = QHBoxLayout()
        label_layout_l_thigh.addWidget(label_l_thigh)
        label_layout_l_thigh.addWidget(self.combobox_l_thigh)
        left_layout.addLayout(label_layout_l_thigh)

        label_l_leg = QLabel("l_leg:")
        self.combobox_l_leg = QComboBox()
        for key in l_leg.keys():
            l_leg_item_id = l_leg[key]["item_id"]
            self.combobox_l_leg.addItem(
                QIcon(
                    f"images/{l_leg_item_id}.png"
                ),
                key,
            )

        label_layout_l_leg = QHBoxLayout()
        label_layout_l_leg.addWidget(label_l_leg)
        label_layout_l_leg.addWidget(self.combobox_l_leg)
        right_layout.addLayout(label_layout_l_leg)

        label_r_leg = QLabel("r_leg:")
        self.combobox_r_leg = QComboBox()
        for key in r_leg.keys():
            r_leg_item_id = r_leg[key]["item_id"]
            self.combobox_r_leg.addItem(
                QIcon(
                    f"images/{r_leg_item_id}.png"
                ),
                key,
            )

        label_layout_r_leg = QHBoxLayout()
        label_layout_r_leg.addWidget(label_r_leg)
        label_layout_r_leg.addWidget(self.combobox_r_leg)
        left_layout.addLayout(label_layout_r_leg)

        label_r_foot = QLabel("r_foot:")
        self.combobox_r_foot = QComboBox()
        for key in r_foot.keys():
            r_foot_item_id = r_foot[key]["item_id"]
            self.combobox_r_foot.addItem(
                QIcon(
                    f"images/{r_foot_item_id}.png"
                ),
                key,
            )

        label_layout_r_foot = QHBoxLayout()
        label_layout_r_foot.addWidget(label_r_foot)
        label_layout_r_foot.addWidget(self.combobox_r_foot)
        right_layout.addLayout(label_layout_r_foot)

        label_l_foot = QLabel("l_foot:")
        self.combobox_l_foot = QComboBox()
        for key in l_foot.keys():
            l_foot_item_id = l_foot[key]["item_id"]
            self.combobox_l_foot.addItem(
                QIcon(
                    f"images/{l_foot_item_id}.png"
                ),
                key,
            )

        label_layout_l_foot = QHBoxLayout()
        label_layout_l_foot.addWidget(label_l_foot)
        label_layout_l_foot.addWidget(self.combobox_l_foot)
        left_layout.addLayout(label_layout_l_foot)

        label_j_neck = QLabel("j_neck:")
        self.combobox_j_neck = QComboBox()
        for key in j_neck.keys():
            j_neck_item_id = j_neck[key]["item_id"]
            self.combobox_j_neck.addItem(
                QIcon(
                    f"images/{j_neck_item_id}.png"
                ),
                key,
            )

        label_layout_j_neck = QHBoxLayout()
        label_layout_j_neck.addWidget(label_j_neck)
        label_layout_j_neck.addWidget(self.combobox_j_neck)
        right_layout.addLayout(label_layout_j_neck)

        label_j_chest = QLabel("j_chest:")
        self.combobox_j_chest = QComboBox()
        for key in j_chest.keys():
            j_chest_item_id = j_chest[key]["item_id"]
            self.combobox_j_chest.addItem(
                QIcon(
                    f"images/{j_chest_item_id}.png"
                ),
                key,
            )

        label_layout_j_chest = QHBoxLayout()
        label_layout_j_chest.addWidget(label_j_chest)
        label_layout_j_chest.addWidget(self.combobox_j_chest)
        left_layout.addLayout(label_layout_j_chest)

        label_j_lumbar = QLabel("j_lumbar:")
        self.combobox_j_lumbar = QComboBox()
        for key in j_lumbar.keys():
            j_lumbar_item_id = j_lumbar[key]["item_id"]
            self.combobox_j_lumbar.addItem(
                QIcon(
                    f"images/{j_lumbar_item_id}.png"
                ),
                key,
            )

        label_layout_j_lumbar = QHBoxLayout()
        label_layout_j_lumbar.addWidget(label_j_lumbar)
        label_layout_j_lumbar.addWidget(self.combobox_j_lumbar)
        right_layout.addLayout(label_layout_j_lumbar)

        label_j_abs = QLabel("j_abs:")
        self.combobox_j_abs = QComboBox()
        for key in j_abs.keys():
            j_abs_item_id = j_abs[key]["item_id"]
            self.combobox_j_abs.addItem(
                QIcon(
                    f"images/{j_abs_item_id}.png"
                ),
                key,
            )

        label_layout_j_abs = QHBoxLayout()
        label_layout_j_abs.addWidget(label_j_abs)
        label_layout_j_abs.addWidget(self.combobox_j_abs)
        left_layout.addLayout(label_layout_j_abs)

        label_j_r_pecs = QLabel("j_r_pecs:")
        self.combobox_j_r_pecs = QComboBox()
        for key in j_r_pecs.keys():
            j_r_pecs_item_id = j_r_pecs[key]["item_id"]
            self.combobox_j_r_pecs.addItem(
                QIcon(
                    f"images/{j_r_pecs_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_pecs = QHBoxLayout()
        label_layout_j_r_pecs.addWidget(label_j_r_pecs)
        label_layout_j_r_pecs.addWidget(self.combobox_j_r_pecs)
        right_layout.addLayout(label_layout_j_r_pecs)

        label_j_r_shoulder = QLabel("j_r_shoulder:")
        self.combobox_j_r_shoulder = QComboBox()
        for key in j_r_shoulder.keys():
            j_r_shoulder_item_id = j_r_shoulder[key]["item_id"]
            self.combobox_j_r_shoulder.addItem(
                QIcon(
                    f"images/{j_r_shoulder_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_shoulder = QHBoxLayout()
        label_layout_j_r_shoulder.addWidget(label_j_r_shoulder)
        label_layout_j_r_shoulder.addWidget(self.combobox_j_r_shoulder)
        left_layout.addLayout(label_layout_j_r_shoulder)

        label_j_r_elbow = QLabel("j_r_elbow:")
        self.combobox_j_r_elbow = QComboBox()
        for key in j_r_elbow.keys():
            j_r_elbow_item_id = j_r_elbow[key]["item_id"]
            self.combobox_j_r_elbow.addItem(
                QIcon(
                    f"images/{j_r_elbow_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_elbow = QHBoxLayout()
        label_layout_j_r_elbow.addWidget(label_j_r_elbow)
        label_layout_j_r_elbow.addWidget(self.combobox_j_r_elbow)
        right_layout.addLayout(label_layout_j_r_elbow)

        label_j_l_pecs = QLabel("j_l_pecs:")
        self.combobox_j_l_pecs = QComboBox()
        for key in j_l_pecs.keys():
            j_l_pecs_item_id = j_l_pecs[key]["item_id"]
            self.combobox_j_l_pecs.addItem(
                QIcon(
                    f"images/{j_l_pecs_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_pecs = QHBoxLayout()
        label_layout_j_l_pecs.addWidget(label_j_l_pecs)
        label_layout_j_l_pecs.addWidget(self.combobox_j_l_pecs)
        left_layout.addLayout(label_layout_j_l_pecs)

        label_j_l_shoulder = QLabel("j_l_shoulder:")
        self.combobox_j_l_shoulder = QComboBox()
        for key in j_l_shoulder.keys():
            j_l_shoulder_item_id = j_l_shoulder[key]["item_id"]
            self.combobox_j_l_shoulder.addItem(
                QIcon(
                    f"images/{j_l_shoulder_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_shoulder = QHBoxLayout()
        label_layout_j_l_shoulder.addWidget(label_j_l_shoulder)
        label_layout_j_l_shoulder.addWidget(self.combobox_j_l_shoulder)
        right_layout.addLayout(label_layout_j_l_shoulder)

        label_j_l_elbow = QLabel("j_l_elbow:")
        self.combobox_j_l_elbow = QComboBox()
        for key in j_l_elbow.keys():
            j_l_elbow_item_id = j_l_elbow[key]["item_id"]
            self.combobox_j_l_elbow.addItem(
                QIcon(
                    f"images/{j_l_elbow_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_elbow = QHBoxLayout()
        label_layout_j_l_elbow.addWidget(label_j_l_elbow)
        label_layout_j_l_elbow.addWidget(self.combobox_j_l_elbow)
        left_layout.addLayout(label_layout_j_l_elbow)

        label_j_r_wrist = QLabel("j_r_wrist:")
        self.combobox_j_r_wrist = QComboBox()
        for key in j_r_wrist.keys():
            j_r_wrist_item_id = j_r_wrist[key]["item_id"]
            self.combobox_j_r_wrist.addItem(
                QIcon(
                    f"images/{j_r_wrist_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_wrist = QHBoxLayout()
        label_layout_j_r_wrist.addWidget(label_j_r_wrist)
        label_layout_j_r_wrist.addWidget(self.combobox_j_r_wrist)
        right_layout.addLayout(label_layout_j_r_wrist)

        label_j_l_wrist = QLabel("j_l_wrist:")
        self.combobox_j_l_wrist = QComboBox()
        for key in j_l_wrist.keys():
            j_l_wrist_item_id = j_l_wrist[key]["item_id"]
            self.combobox_j_l_wrist.addItem(
                QIcon(
                    f"images/{j_l_wrist_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_wrist = QHBoxLayout()
        label_layout_j_l_wrist.addWidget(label_j_l_wrist)
        label_layout_j_l_wrist.addWidget(self.combobox_j_l_wrist)
        left_layout.addLayout(label_layout_j_l_wrist)

        label_j_r_glute = QLabel("j_r_glute:")
        self.combobox_j_r_glute = QComboBox()
        for key in j_r_glute.keys():
            j_r_glute_item_id = j_r_glute[key]["item_id"]
            self.combobox_j_r_glute.addItem(
                QIcon(
                    f"images/{j_r_glute_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_glute = QHBoxLayout()
        label_layout_j_r_glute.addWidget(label_j_r_glute)
        label_layout_j_r_glute.addWidget(self.combobox_j_r_glute)
        right_layout.addLayout(label_layout_j_r_glute)

        label_j_l_glute = QLabel("j_l_glute:")
        self.combobox_j_l_glute = QComboBox()
        for key in j_l_glute.keys():
            j_l_glute_item_id = j_l_glute[key]["item_id"]
            self.combobox_j_l_glute.addItem(
                QIcon(
                    f"images/{j_l_glute_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_glute = QHBoxLayout()
        label_layout_j_l_glute.addWidget(label_j_l_glute)
        label_layout_j_l_glute.addWidget(self.combobox_j_l_glute)
        left_layout.addLayout(label_layout_j_l_glute)

        label_j_r_hip = QLabel("j_r_hip:")
        self.combobox_j_r_hip = QComboBox()
        for key in j_r_hip.keys():
            j_r_hip_item_id = j_r_hip[key]["item_id"]
            self.combobox_j_r_hip.addItem(
                QIcon(
                    f"images/{j_r_hip_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_hip = QHBoxLayout()
        label_layout_j_r_hip.addWidget(label_j_r_hip)
        label_layout_j_r_hip.addWidget(self.combobox_j_r_hip)
        right_layout.addLayout(label_layout_j_r_hip)

        label_j_l_hip = QLabel("j_l_hip:")
        self.combobox_j_l_hip = QComboBox()
        for key in j_l_hip.keys():
            j_l_hip_item_id = j_l_hip[key]["item_id"]
            self.combobox_j_l_hip.addItem(
                QIcon(
                    f"images/{j_l_hip_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_hip = QHBoxLayout()
        label_layout_j_l_hip.addWidget(label_j_l_hip)
        label_layout_j_l_hip.addWidget(self.combobox_j_l_hip)
        left_layout.addLayout(label_layout_j_l_hip)

        label_j_r_knee = QLabel("j_r_knee:")
        self.combobox_j_r_knee = QComboBox()
        for key in j_r_knee.keys():
            j_r_knee_item_id = j_r_knee[key]["item_id"]
            self.combobox_j_r_knee.addItem(
                QIcon(
                    f"images/{j_r_knee_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_knee = QHBoxLayout()
        label_layout_j_r_knee.addWidget(label_j_r_knee)
        label_layout_j_r_knee.addWidget(self.combobox_j_r_knee)
        right_layout.addLayout(label_layout_j_r_knee)

        label_j_l_knee = QLabel("j_l_knee:")
        self.combobox_j_l_knee = QComboBox()
        for key in j_l_knee.keys():
            j_l_knee_item_id = j_l_knee[key]["item_id"]
            self.combobox_j_l_knee.addItem(
                QIcon(
                    f"images/{j_l_knee_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_knee = QHBoxLayout()
        label_layout_j_l_knee.addWidget(label_j_l_knee)
        label_layout_j_l_knee.addWidget(self.combobox_j_l_knee)
        left_layout.addLayout(label_layout_j_l_knee)

        label_j_r_ankle = QLabel("j_r_ankle:")
        self.combobox_j_r_ankle = QComboBox()
        for key in j_r_ankle.keys():
            j_r_ankle_item_id = j_r_ankle[key]["item_id"]
            self.combobox_j_r_ankle.addItem(
                QIcon(
                    f"images/{j_r_ankle_item_id}.png"
                ),
                key,
            )

        label_layout_j_r_ankle = QHBoxLayout()
        label_layout_j_r_ankle.addWidget(label_j_r_ankle)
        label_layout_j_r_ankle.addWidget(self.combobox_j_r_ankle)
        right_layout.addLayout(label_layout_j_r_ankle)

        label_j_l_ankle = QLabel("j_l_ankle:")
        self.combobox_j_l_ankle = QComboBox()
        for key in j_l_ankle.keys():
            j_l_ankle_item_id = j_l_ankle[key]["item_id"]
            self.combobox_j_l_ankle.addItem(
                QIcon(
                    f"images/{j_l_ankle_item_id}.png"
                ),
                key,
            )

        label_layout_j_l_ankle = QHBoxLayout()
        label_layout_j_l_ankle.addWidget(label_j_l_ankle)
        label_layout_j_l_ankle.addWidget(self.combobox_j_l_ankle)
        left_layout.addLayout(label_layout_j_l_ankle)

        self.comboboxes = [
            self.combobox_head,
            self.combobox_breast,
            self.combobox_chest,
            self.combobox_stomach,
            self.combobox_groin,
            self.combobox_r_pecs,
            self.combobox_r_biceps,
            self.combobox_r_triceps,
            self.combobox_l_pecs,
            self.combobox_l_biceps,
            self.combobox_l_triceps,
            self.combobox_r_hand,
            self.combobox_l_hand,
            self.combobox_r_butt,
            self.combobox_l_butt,
            self.combobox_r_thigh,
            self.combobox_l_thigh,
            self.combobox_l_leg,
            self.combobox_r_leg,
            self.combobox_r_foot,
            self.combobox_l_foot,
            self.combobox_j_neck,
            self.combobox_j_chest,
            self.combobox_j_lumbar,
            self.combobox_j_abs,
            self.combobox_j_r_pecs,
            self.combobox_j_r_shoulder,
            self.combobox_j_r_elbow,
            self.combobox_j_l_pecs,
            self.combobox_j_l_shoulder,
            self.combobox_j_l_elbow,
            self.combobox_j_r_wrist,
            self.combobox_j_l_wrist,
            self.combobox_j_r_glute,
            self.combobox_j_l_glute,
            self.combobox_j_r_hip,
            self.combobox_j_l_hip,
            self.combobox_j_r_knee,
            self.combobox_j_l_knee,
            self.combobox_j_r_ankle,
            self.combobox_j_l_ankle,
        ]
        self.dict = {
            "head": head,
            "breast": breast,
            "chest": chest,
            "stomach": stomach,
            "groin": groin,
            "r_pecs": r_pecs,
            "r_biceps": r_biceps,
            "r_triceps": r_triceps,
            "l_pecs": l_pecs,
            "l_biceps": l_biceps,
            "l_triceps": l_triceps,
            "r_hand": r_hand,
            "l_hand": l_hand,
            "r_butt": r_butt,
            "l_butt": l_butt,
            "r_thigh": r_thigh,
            "l_thigh": l_thigh,
            "l_leg": l_leg,
            "r_leg": r_leg,
            "r_foot": r_foot,
            "l_foot": l_foot,
            "j_neck": j_neck,
            "j_chest": j_chest,
            "j_lumbar": j_lumbar,
            "j_abs": j_abs,
            "j_r_pecs": j_r_pecs,
            "j_r_shoulder": j_r_shoulder,
            "j_r_elbow": j_r_elbow,
            "j_l_pecs": j_l_pecs,
            "j_l_shoulder": j_l_shoulder,
            "j_l_elbow": j_l_elbow,
            "j_r_wrist": j_r_wrist,
            "j_l_wrist": j_l_wrist,
            "j_r_glute": j_r_glute,
            "j_l_glute": j_l_glute,
            "j_r_hip": j_r_hip,
            "j_l_hip": j_l_hip,
            "j_r_knee": j_r_knee,
            "j_l_knee": j_l_knee,
            "j_r_ankle": j_r_ankle,
            "j_l_ankle": j_l_ankle,
        }



    def setup_tab2(self):
        main_layout2 = QVBoxLayout()
        self.tab2.setLayout(main_layout2)

        label_force_color = QLabel("Force Color:")
        self.dropdown_force_color = QComboBox()
        self.dropdown_force_color.addItems(dropdown_values)
        layout_force_color = QHBoxLayout()
        layout_force_color.addWidget(label_force_color)
        layout_force_color.addWidget(self.dropdown_force_color)
        main_layout2.addLayout(layout_force_color)

        label_relax_color = QLabel("Relax Color:")
        self.dropdown_relax_color = QComboBox()
        self.dropdown_relax_color.addItems(dropdown_values)
        layout_relax_color = QHBoxLayout()
        layout_relax_color.addWidget(label_relax_color)
        layout_relax_color.addWidget(self.dropdown_relax_color)
        main_layout2.addLayout(layout_relax_color)

        label_torso_color = QLabel("Torso Color:")
        self.dropdown_torso_color = QComboBox()
        self.dropdown_torso_color.addItems(dropdown_values)
        layout_torso_color = QHBoxLayout()
        layout_torso_color.addWidget(label_torso_color)
        layout_torso_color.addWidget(self.dropdown_torso_color)
        main_layout2.addLayout(layout_torso_color)

        label_ghost_color = QLabel("Ghost Color:")
        self.dropdown_ghost_color = QComboBox()
        self.dropdown_ghost_color.addItems(dropdown_values)
        layout_ghost_color = QHBoxLayout()
        layout_ghost_color.addWidget(label_ghost_color)
        layout_ghost_color.addWidget(self.dropdown_ghost_color)
        main_layout2.addLayout(layout_ghost_color)

        label_blood_color = QLabel("Blood Color:")
        self.dropdown_blood_color = QComboBox()
        self.dropdown_blood_color.addItems(dropdown_values)
        layout_blood_color = QHBoxLayout()
        layout_blood_color.addWidget(label_blood_color)
        layout_blood_color.addWidget(self.dropdown_blood_color)
        main_layout2.addLayout(layout_blood_color)
        
        label_dq_ring_color = QLabel("DQ Ring Color:")
        self.dropdown_dq_ring_color = QComboBox()
        self.dropdown_dq_ring_color.addItems(dropdown_values)
        layout_dq_ring_color = QHBoxLayout()
        layout_dq_ring_color.addWidget(label_dq_ring_color)
        layout_dq_ring_color.addWidget(self.dropdown_dq_ring_color)
        main_layout2.addLayout(layout_dq_ring_color)

        label_timer_color = QLabel("Timer Color:")
        self.dropdown_timer_color = QComboBox()
        self.dropdown_timer_color.addItems(dropdown_values)
        layout_timer_color = QHBoxLayout()
        layout_timer_color.addWidget(label_timer_color)
        layout_timer_color.addWidget(self.dropdown_timer_color)
        main_layout2.addLayout(layout_timer_color)

        label_user_text_color = QLabel("User Text Color:")
        self.dropdown_user_text_color = QComboBox()
        self.dropdown_user_text_color.addItems(dropdown_values)
        layout_user_text_color = QHBoxLayout()
        layout_user_text_color.addWidget(label_user_text_color)
        layout_user_text_color.addWidget(self.dropdown_user_text_color)
        main_layout2.addLayout(layout_user_text_color)

        label_emote_color = QLabel("Emote Color:")
        self.dropdown_emote_color = QComboBox()
        self.dropdown_emote_color.addItems(dropdown_values)
        layout_emote_color = QHBoxLayout()
        layout_emote_color.addWidget(label_emote_color)
        layout_emote_color.addWidget(self.dropdown_emote_color)
        main_layout2.addLayout(layout_emote_color)

        label_grip_color = QLabel("Grip Color:")
        self.dropdown_grip_color = QComboBox()
        self.dropdown_grip_color.addItems(dropdown_values)
        layout_grip_color = QHBoxLayout()
        layout_grip_color.addWidget(label_grip_color)
        layout_grip_color.addWidget(self.dropdown_grip_color)
        main_layout2.addLayout(layout_grip_color)

        label_gradcol1_color = QLabel("Primary Gradient Color:")
        self.dropdown_gradcol1_color = QComboBox()
        self.dropdown_gradcol1_color.addItems(dropdown_values)
        layout_gradcol1_color = QHBoxLayout()
        layout_gradcol1_color.addWidget(label_gradcol1_color)
        layout_gradcol1_color.addWidget(self.dropdown_gradcol1_color)
        main_layout2.addLayout(layout_gradcol1_color)

        label_gradcol2_color = QLabel("Secondary Gradient Color:")
        self.dropdown_gradcol2_color = QComboBox()
        self.dropdown_gradcol2_color.addItems(dropdown_values)
        layout_gradcol2_color = QHBoxLayout()
        layout_gradcol2_color.addWidget(label_gradcol2_color)
        layout_gradcol2_color.addWidget(self.dropdown_gradcol2_color)
        main_layout2.addLayout(layout_gradcol2_color)

    def select_file(self):
        file_dialog = QFileDialog()
        
        folder_path = file_dialog.getExistingDirectory(
            self, "Select Destination Folder"
        )
        if folder_path:
            self.file_text.setText(folder_path)
            self.item_dat_path = os.path.join(folder_path, "item.dat")
            if not os.path.isfile(self.item_dat_path):
                self.apply_button.setEnabled(False)
                QMessageBox.warning(
                    self,
                    "Missing File",
                    "Please select a folder containing the 'item.dat' file.",
                )
                return
            else:
                self.apply_button.setEnabled(True)

    def modify_force(self):
        file_path = self.file_text.text()+"/item.dat"

        self.file_perms_op()

        if not file_path:
            return

        color = self.dropdown_force_color.currentText()

        if color in color_id:
            color_code = color_id[color]

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
        self.file_perms_cl()

            


    def modify_relax(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
            return

        color = self.dropdown_relax_color.currentText()

        if color in color_id:
            color_code = color_id[color]

        with open(file_path, 'r') as file:
            lines = file.readlines()

        words = lines[7].split()
        words[2::2] = [str(color_code)] * 21
        words[-1] = '0'
        lines[7] = ' '.join(words) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)
        self.file_perms_cl()

        
            


    def modify_torso(self):
        initial_string = "BODCOL 0;0 x 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 x 12 x 13 x 14 x 15 x 16 x 17 x 18 x 19 x 20 x\n"
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()
        
        
            
        

    def modify_ghost(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()

        
    def modify_blood(self):
        file_path = self.file_text.text() + "/item.dat"
        self.file_perms_op()
        if not file_path:
            return

        color = self.dropdown_blood_color.currentText()
        if color in color_id:
            color_code = color_id[color]

        with open(file_path, "r") as file:
            lines = file.readlines()

        words = lines[2].split()
        words[1] = "0;" + str(color_code)
        lines[2] = " ".join(words) + "\n"

        with open(file_path, "w") as file:
            file.writelines(lines)
        self.file_perms_cl()



    def modify_dq_ring(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()


    def modify_timer(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()

        
    def modify_usertext(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
            return

        color = self.dropdown_user_text_color.currentText()
        if color in color_id:
            color_code = color_id[color]    
        with open(file_path, "r") as file:    
            lines = file.readlines()

        
        words = lines[2].split()
        words[12] = str(color_code)
        lines[2] = " ".join(words) + "\n"

        
        with open(file_path, "w") as file:
            file.writelines(lines)
        self.file_perms_cl()
            

    def modify_emote(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()

        
            

    def modify_grip(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()

        
            

    def modify_gradcol1(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()


    def modify_gradcol2(self):
        file_path = self.file_text.text()+"/item.dat"
        self.file_perms_op()
        if not file_path:
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
        self.file_perms_cl()
            

    def modify_item_value(self, selected_item, dictionaries):
        self.file_perms_op()
        item_values = None
        for dictionary_name, dictionary in dictionaries.items():
            if selected_item in dictionary:
                item_values = dictionary[selected_item]
                break

        if item_values is None:
            self.console.insertPlainText(
                "The selected item was not found in the dictionaries."
            )
            return

        body_id = int(item_values["bodyid"]) 
        if body_id > 20:
            joint_id = body_id - 21
            line_prefix = "OBJJOINT"
        else:
            joint_id = body_id
            line_prefix = "OBJ"

        color_id = item_values["color"]
        alpha = item_values["alpha"]
        dynamic = item_values["dynamic"]
        partless = item_values["partless"]

        with open(self.item_dat_path, "r") as file:
            lines = file.readlines()

        with open(self.item_dat_path, "w") as file:
            for line in lines:
                line_parts = line.split()
                if line_parts[0].startswith(line_prefix):
                    if line_parts[0] == line_prefix + str(joint_id):
                        modified_line = f"{line_prefix}{joint_id} 1; 1 {color_id} {alpha} 1 {dynamic} {partless} 1\n"
                        file.write(modified_line)
                        if line.strip() != modified_line.strip():
                            self.console.insertPlainText(
                                f"Modified line : {line.strip()} -> {modified_line.strip()}\n"
                            )
                    else:
                        file.write(line)
                else:
                    file.write(line)
        self.file_perms_cl()

    def download_files(self, id, file_path, key):
        if id is None:
            filename = f"{key}.obj"
            file_full_path = os.path.join(file_path, filename)
            if os.path.exists(file_full_path):
                os.remove(file_full_path)
                self.console.insertPlainText(f"The file {filename} has been deleted.\n")
            filename = f"{key}_obj.tga"
            file_full_path = os.path.join(file_path, filename)
            if os.path.exists(file_full_path):
                os.remove(file_full_path)
                self.console.insertPlainText(f"The file {filename} has been deleted.\n")
            return

        base_url = "https://cache.toribash.com/objects/"
        file_extensions = [".obj", ".tga"]

        for extension in file_extensions:
            url = f"{base_url}{id}{extension}"
            if extension == ".tga":
                filename = f"{key}_obj{extension}"
            else:
                filename = f"{key}{extension}"
            file_full_path = os.path.join(
                file_path, filename
            )  

            response = requests.get(url)

            if response.status_code == 200:
                with open(file_full_path, "wb") as file:
                    file.write(response.content)
                self.console.insertPlainText(
                    f"The file {filename} was downloaded successfully.\n"
                )
            else:
                self.console.insertPlainText(
                    f"Error downloading the file {filename}.\n"
                )

    def apply_button_clicked(self):
        self.console.clear()
        selected_values = [combobox.currentText() for combobox in self.comboboxes]
        self.modify_all_colors()

        for key, value in zip(self.dict.keys(), selected_values):
            if value != "None":
                item_id = self.dict[key][value]["item_id"]
                file_path = os.path.dirname(
                    self.item_dat_path
                )  
                self.download_files(item_id, file_path, key)
                dictionary = self.dict
                self.modify_item_value(value, dictionary)
            else:
                file_path = os.path.dirname(
                    self.item_dat_path
                ) 
                self.download_files(id=None, file_path=file_path, key=key)

    def modify_all_colors(self):
        self.modify_force()
        self.modify_relax()
        self.modify_torso()
        self.modify_ghost()
        self.modify_blood()
        self.modify_dq_ring()
        self.modify_timer()
        self.modify_usertext()
        self.modify_emote()
        self.modify_grip()
        self.modify_gradcol1()
        self.modify_gradcol2()
        QMessageBox.information(self, "Sucess", "All colors have been modified successfully.")

    def file_perms_op(self):
        if os.path.exists(self.item_dat_path):
            permissions = os.stat(self.item_dat_path).st_mode
            nouveau_permissions = permissions | 0o222
            os.chmod(self.item_dat_path, nouveau_permissions)

    def file_perms_cl(self):
        if os.path.exists(self.item_dat_path):
            permissions = os.stat(self.item_dat_path).st_mode
            nouveau_permissions = permissions & ~0o222
            os.chmod(self.item_dat_path, nouveau_permissions)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    maxWidth = 200
    style = "QComboBox { min-width: %spx; max-width: %spx; }" % (maxWidth, maxWidth)
    window.setStyleSheet(style)
    window.show()
    sys.exit(app.exec_())

