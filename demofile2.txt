//
//  ViewController.swift
//  CommonInputControls
//
//  Created by Drew Dodson on 2/25/20.
//  Copyright © 2020 Arcalla.com. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
    }



    @IBAction func buttonTapped(_ sender: UIButton) {
        print("Button was tapped.")
    }
    @IBAction func switchToggled(_ sender: UISwitch) {
        if sender.isOn {
            print("The switch is on.")
        } else {
            print("The switch is off.")
        }
    }
    @IBAction func sliderChanged(_ sender: UISlider) {
        print(sender.value)
    }
    @IBAction func textFieldChanged(_ sender: UITextField) {
        if let text = sender.text {
            print(text)
        }
    }
    @IBAction func textFieldChanged2(_ sender: UITextField) {
        if let text = sender.text {
            print(text)
        }
    }
    @IBAction func gestureRecognized(_ sender: UITapGestureRecognizer) {
        let location = sender.location(in: view)
        print(location)
    }
    




// LAST } IN THE ViewContoller Class
}
