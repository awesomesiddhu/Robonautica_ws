// Auto-generated. Do not edit!

// (in-package tortoisebotpromax_firmware.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Diff {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ldir = null;
      this.lpwm = null;
      this.rdir = null;
      this.rpwm = null;
    }
    else {
      if (initObj.hasOwnProperty('ldir')) {
        this.ldir = initObj.ldir
      }
      else {
        this.ldir = new std_msgs.msg.Bool();
      }
      if (initObj.hasOwnProperty('lpwm')) {
        this.lpwm = initObj.lpwm
      }
      else {
        this.lpwm = new std_msgs.msg.UInt8();
      }
      if (initObj.hasOwnProperty('rdir')) {
        this.rdir = initObj.rdir
      }
      else {
        this.rdir = new std_msgs.msg.Bool();
      }
      if (initObj.hasOwnProperty('rpwm')) {
        this.rpwm = initObj.rpwm
      }
      else {
        this.rpwm = new std_msgs.msg.UInt8();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Diff
    // Serialize message field [ldir]
    bufferOffset = std_msgs.msg.Bool.serialize(obj.ldir, buffer, bufferOffset);
    // Serialize message field [lpwm]
    bufferOffset = std_msgs.msg.UInt8.serialize(obj.lpwm, buffer, bufferOffset);
    // Serialize message field [rdir]
    bufferOffset = std_msgs.msg.Bool.serialize(obj.rdir, buffer, bufferOffset);
    // Serialize message field [rpwm]
    bufferOffset = std_msgs.msg.UInt8.serialize(obj.rpwm, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Diff
    let len;
    let data = new Diff(null);
    // Deserialize message field [ldir]
    data.ldir = std_msgs.msg.Bool.deserialize(buffer, bufferOffset);
    // Deserialize message field [lpwm]
    data.lpwm = std_msgs.msg.UInt8.deserialize(buffer, bufferOffset);
    // Deserialize message field [rdir]
    data.rdir = std_msgs.msg.Bool.deserialize(buffer, bufferOffset);
    // Deserialize message field [rpwm]
    data.rpwm = std_msgs.msg.UInt8.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'tortoisebotpromax_firmware/Diff';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ef331214eeb33030643446a132be9599';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Bool ldir
    std_msgs/UInt8 lpwm
    std_msgs/Bool rdir
    std_msgs/UInt8 rpwm
    ================================================================================
    MSG: std_msgs/Bool
    bool data
    ================================================================================
    MSG: std_msgs/UInt8
    uint8 data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Diff(null);
    if (msg.ldir !== undefined) {
      resolved.ldir = std_msgs.msg.Bool.Resolve(msg.ldir)
    }
    else {
      resolved.ldir = new std_msgs.msg.Bool()
    }

    if (msg.lpwm !== undefined) {
      resolved.lpwm = std_msgs.msg.UInt8.Resolve(msg.lpwm)
    }
    else {
      resolved.lpwm = new std_msgs.msg.UInt8()
    }

    if (msg.rdir !== undefined) {
      resolved.rdir = std_msgs.msg.Bool.Resolve(msg.rdir)
    }
    else {
      resolved.rdir = new std_msgs.msg.Bool()
    }

    if (msg.rpwm !== undefined) {
      resolved.rpwm = std_msgs.msg.UInt8.Resolve(msg.rpwm)
    }
    else {
      resolved.rpwm = new std_msgs.msg.UInt8()
    }

    return resolved;
    }
};

module.exports = Diff;
