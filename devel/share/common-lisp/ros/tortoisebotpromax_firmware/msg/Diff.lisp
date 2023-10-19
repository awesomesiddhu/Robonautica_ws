; Auto-generated. Do not edit!


(cl:in-package tortoisebotpromax_firmware-msg)


;//! \htmlinclude Diff.msg.html

(cl:defclass <Diff> (roslisp-msg-protocol:ros-message)
  ((ldir
    :reader ldir
    :initarg :ldir
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (lpwm
    :reader lpwm
    :initarg :lpwm
    :type std_msgs-msg:UInt8
    :initform (cl:make-instance 'std_msgs-msg:UInt8))
   (rdir
    :reader rdir
    :initarg :rdir
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (rpwm
    :reader rpwm
    :initarg :rpwm
    :type std_msgs-msg:UInt8
    :initform (cl:make-instance 'std_msgs-msg:UInt8)))
)

(cl:defclass Diff (<Diff>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Diff>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Diff)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tortoisebotpromax_firmware-msg:<Diff> is deprecated: use tortoisebotpromax_firmware-msg:Diff instead.")))

(cl:ensure-generic-function 'ldir-val :lambda-list '(m))
(cl:defmethod ldir-val ((m <Diff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tortoisebotpromax_firmware-msg:ldir-val is deprecated.  Use tortoisebotpromax_firmware-msg:ldir instead.")
  (ldir m))

(cl:ensure-generic-function 'lpwm-val :lambda-list '(m))
(cl:defmethod lpwm-val ((m <Diff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tortoisebotpromax_firmware-msg:lpwm-val is deprecated.  Use tortoisebotpromax_firmware-msg:lpwm instead.")
  (lpwm m))

(cl:ensure-generic-function 'rdir-val :lambda-list '(m))
(cl:defmethod rdir-val ((m <Diff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tortoisebotpromax_firmware-msg:rdir-val is deprecated.  Use tortoisebotpromax_firmware-msg:rdir instead.")
  (rdir m))

(cl:ensure-generic-function 'rpwm-val :lambda-list '(m))
(cl:defmethod rpwm-val ((m <Diff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tortoisebotpromax_firmware-msg:rpwm-val is deprecated.  Use tortoisebotpromax_firmware-msg:rpwm instead.")
  (rpwm m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Diff>) ostream)
  "Serializes a message object of type '<Diff>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ldir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'lpwm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'rdir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'rpwm) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Diff>) istream)
  "Deserializes a message object of type '<Diff>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ldir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'lpwm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'rdir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'rpwm) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Diff>)))
  "Returns string type for a message object of type '<Diff>"
  "tortoisebotpromax_firmware/Diff")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Diff)))
  "Returns string type for a message object of type 'Diff"
  "tortoisebotpromax_firmware/Diff")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Diff>)))
  "Returns md5sum for a message object of type '<Diff>"
  "ef331214eeb33030643446a132be9599")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Diff)))
  "Returns md5sum for a message object of type 'Diff"
  "ef331214eeb33030643446a132be9599")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Diff>)))
  "Returns full string definition for message of type '<Diff>"
  (cl:format cl:nil "std_msgs/Bool ldir~%std_msgs/UInt8 lpwm~%std_msgs/Bool rdir~%std_msgs/UInt8 rpwm~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/UInt8~%uint8 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Diff)))
  "Returns full string definition for message of type 'Diff"
  (cl:format cl:nil "std_msgs/Bool ldir~%std_msgs/UInt8 lpwm~%std_msgs/Bool rdir~%std_msgs/UInt8 rpwm~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/UInt8~%uint8 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Diff>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ldir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'lpwm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'rdir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'rpwm))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Diff>))
  "Converts a ROS message object to a list"
  (cl:list 'Diff
    (cl:cons ':ldir (ldir msg))
    (cl:cons ':lpwm (lpwm msg))
    (cl:cons ':rdir (rdir msg))
    (cl:cons ':rpwm (rpwm msg))
))
