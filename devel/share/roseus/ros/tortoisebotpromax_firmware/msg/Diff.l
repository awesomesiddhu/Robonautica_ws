;; Auto-generated. Do not edit!


(when (boundp 'tortoisebotpromax_firmware::Diff)
  (if (not (find-package "TORTOISEBOTPROMAX_FIRMWARE"))
    (make-package "TORTOISEBOTPROMAX_FIRMWARE"))
  (shadow 'Diff (find-package "TORTOISEBOTPROMAX_FIRMWARE")))
(unless (find-package "TORTOISEBOTPROMAX_FIRMWARE::DIFF")
  (make-package "TORTOISEBOTPROMAX_FIRMWARE::DIFF"))

(in-package "ROS")
;;//! \htmlinclude Diff.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass tortoisebotpromax_firmware::Diff
  :super ros::object
  :slots (_ldir _lpwm _rdir _rpwm ))

(defmethod tortoisebotpromax_firmware::Diff
  (:init
   (&key
    ((:ldir __ldir) (instance std_msgs::Bool :init))
    ((:lpwm __lpwm) (instance std_msgs::UInt8 :init))
    ((:rdir __rdir) (instance std_msgs::Bool :init))
    ((:rpwm __rpwm) (instance std_msgs::UInt8 :init))
    )
   (send-super :init)
   (setq _ldir __ldir)
   (setq _lpwm __lpwm)
   (setq _rdir __rdir)
   (setq _rpwm __rpwm)
   self)
  (:ldir
   (&rest __ldir)
   (if (keywordp (car __ldir))
       (send* _ldir __ldir)
     (progn
       (if __ldir (setq _ldir (car __ldir)))
       _ldir)))
  (:lpwm
   (&rest __lpwm)
   (if (keywordp (car __lpwm))
       (send* _lpwm __lpwm)
     (progn
       (if __lpwm (setq _lpwm (car __lpwm)))
       _lpwm)))
  (:rdir
   (&rest __rdir)
   (if (keywordp (car __rdir))
       (send* _rdir __rdir)
     (progn
       (if __rdir (setq _rdir (car __rdir)))
       _rdir)))
  (:rpwm
   (&rest __rpwm)
   (if (keywordp (car __rpwm))
       (send* _rpwm __rpwm)
     (progn
       (if __rpwm (setq _rpwm (car __rpwm)))
       _rpwm)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Bool _ldir
    (send _ldir :serialization-length)
    ;; std_msgs/UInt8 _lpwm
    (send _lpwm :serialization-length)
    ;; std_msgs/Bool _rdir
    (send _rdir :serialization-length)
    ;; std_msgs/UInt8 _rpwm
    (send _rpwm :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Bool _ldir
       (send _ldir :serialize s)
     ;; std_msgs/UInt8 _lpwm
       (send _lpwm :serialize s)
     ;; std_msgs/Bool _rdir
       (send _rdir :serialize s)
     ;; std_msgs/UInt8 _rpwm
       (send _rpwm :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Bool _ldir
     (send _ldir :deserialize buf ptr-) (incf ptr- (send _ldir :serialization-length))
   ;; std_msgs/UInt8 _lpwm
     (send _lpwm :deserialize buf ptr-) (incf ptr- (send _lpwm :serialization-length))
   ;; std_msgs/Bool _rdir
     (send _rdir :deserialize buf ptr-) (incf ptr- (send _rdir :serialization-length))
   ;; std_msgs/UInt8 _rpwm
     (send _rpwm :deserialize buf ptr-) (incf ptr- (send _rpwm :serialization-length))
   ;;
   self)
  )

(setf (get tortoisebotpromax_firmware::Diff :md5sum-) "ef331214eeb33030643446a132be9599")
(setf (get tortoisebotpromax_firmware::Diff :datatype-) "tortoisebotpromax_firmware/Diff")
(setf (get tortoisebotpromax_firmware::Diff :definition-)
      "std_msgs/Bool ldir
std_msgs/UInt8 lpwm
std_msgs/Bool rdir
std_msgs/UInt8 rpwm
================================================================================
MSG: std_msgs/Bool
bool data
================================================================================
MSG: std_msgs/UInt8
uint8 data

")



(provide :tortoisebotpromax_firmware/Diff "ef331214eeb33030643446a132be9599")


