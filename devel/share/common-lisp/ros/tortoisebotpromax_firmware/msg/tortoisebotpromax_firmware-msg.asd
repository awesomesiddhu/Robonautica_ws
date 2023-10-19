
(cl:in-package :asdf)

(defsystem "tortoisebotpromax_firmware-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Diff" :depends-on ("_package_Diff"))
    (:file "_package_Diff" :depends-on ("_package"))
  ))