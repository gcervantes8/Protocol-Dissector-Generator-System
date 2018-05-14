-- do not modify this table
local debug_level = {
    DISABLED = 0,
    LEVEL_1  = 1,
    LEVEL_2  = 2
}

-- set this DEBUG to debug_level.LEVEL_1 to enable printing debug_level info
-- set it to debug_level.LEVEL_2 to enable really verbose printing
-- note: this will be overridden by user's preference settings
local DEBUG = debug_level.LEVEL_1

local default_settings =
{
    debug_level  = DEBUG,
    port         = 65333,
    heur_enabled = false,
}

-- for testing purposes, we want to be able to pass in changes to the defaults
-- from the command line; because you can't set lua preferences from the command
-- line using the '-o' switch (the preferences don't exist until this script is
-- loaded, so the command line thinks they're invalid preferences being set)
-- so we pass them in as command arguments insetad, and handle it here:
local args={...} -- get passed-in args
if args and #args > 0 then
    for _, arg in ipairs(args) do
        local name, value = arg:match("(.+)=(.+)")
        if name and value then
            if tonumber(value) then
                value = tonumber(value)
            elseif value == "true" or value == "TRUE" then
                value = true
            elseif value == "false" or value == "FALSE" then
                value = false
            elseif value == "DISABLED" then
                value = debug_level.DISABLED
            elseif value == "LEVEL_1" then
                value = debug_level.LEVEL_1
            elseif value == "LEVEL_2" then
                value = debug_level.LEVEL_2
            else
                error("invalid commandline argument value")
            end
        else
            error("invalid commandline argument syntax")
        end

        default_settings[name] = value
    end
end

local dprint = function() end
local dprint2 = function() end
local function reset_debug_level()
    if default_settings.debug_level > debug_level.DISABLED then
        dprint = function(...)
            print(table.concat({"Lua:", ...}," "))
        end

        if default_settings.debug_level > debug_level.LEVEL_1 then
            dprint2 = dprint
        end
    end
end
-- call it now
reset_debug_level()

dprint2("Wireshark version = ", get_version())
dprint2("Lua version = ", _VERSION)





local c = Proto("ICMP_dissector_built", "Example ICMP protocol")

local c1 = ProtoField.new("ICMP Type", "Type", ftypes.UINT8, nil, base.HEX, nil, "Checks the type of message")

local c3 = ProtoField.new("Code_source", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c4 = ProtoField.new("Code_redirect", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c5 = ProtoField.new("Code_te", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c6 = ProtoField.new("Code_ts", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c7 = ProtoField.new("Code_tsr_tsr", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c8 = ProtoField.new("Code_addrmask_adr_mask", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c9 = ProtoField.new("Code_addrmask_r", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c10 = ProtoField.new("Code_du", "Code", ftypes.UINT8, nil, base.HEX, 0xf, "Code")

local c11 = ProtoField.new("HeaderChecksum_source", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c12 = ProtoField.new("HeaderChecksum_redirect", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c13 = ProtoField.new("HeaderChecksum_te", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c14 = ProtoField.new("HeaderChecksum_ts", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c15 = ProtoField.new("HeaderChecksum_tsr", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c16 = ProtoField.new("HeaderChecksum_adr_mask", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c17 = ProtoField.new("HeaderChecksum_addrmask_r", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c18 = ProtoField.new("HeaderChecksum_du", "HeaderChecksum", ftypes.UINT16, nil, base.HEX, 0xff, "HeaderChecksum")

local c19 = ProtoField.new("Unused_source", "Unused", ftypes.UINT32, nil, base.HEX, 0xffff, "Unused")

local c20 = ProtoField.new("IP_addr_redirect", "IP_addr", ftypes.UINT32, nil, base.HEX, 0xffff, "IP_addr")

local c21 = ProtoField.new("Unused_te", "Unused", ftypes.UINT32, nil, base.HEX, 0xffff, "Unused")

local c22 = ProtoField.new("Identifier_ts", "Identifier", ftypes.UINT16, nil, base.HEX, 0xff, "Identifier")

local c23 = ProtoField.new("Identifier_tsr", "Identifier", ftypes.UINT16, nil, base.HEX, 0xff, "Identifier")

local c24 = ProtoField.new("Identifier_adr_mask", "Identifier", ftypes.UINT16, nil, base.HEX, 0xff, "Identifier")

local c25 = ProtoField.new("Identifier_addrmask_r", "Identifier", ftypes.UINT16, nil, base.HEX, 0xff, "Identifier")

local c26 = ProtoField.new("Unused_du", "Unused", ftypes.UINT16, nil, base.HEX, 0xff, "Unused")

local c27 = ProtoField.new("IP_header_source", "IP_header", ftypes.UINT32, nil, base.HEX, 0xffff, "IP_header")

local c29 = ProtoField.new("IP_header_te", "IP_header", ftypes.UINT32, nil, base.HEX, 0xffff, "IP_header")

local c30 = ProtoField.new("Seq_number_ts", "Seq_number", ftypes.UINT16, nil, base.HEX, 0xff, "Seq_number")

local c31 = ProtoField.new("Seq_number_tsr", "Seq_number", ftypes.UINT16, nil, base.HEX, 0xff, "Seq_number")

local c32 = ProtoField.new("Seq_number_adr_mask", "Seq_number", ftypes.UINT16, nil, base.HEX, 0xff, "Seq_number")

local c33 = ProtoField.new("Seq_number_addrmask_r", "Seq_number", ftypes.UINT16, nil, base.HEX, 0xff, "Seq_number")

local c34 = ProtoField.new("Next_hop_MTU_du", "Next_hop_MTU", ftypes.UINT16, nil, base.HEX, 0xff, "Next_hop_MTU")

local c35 = ProtoField.new("Original_timestamp_ts", "Original_timestamp", ftypes.UINT32, nil, base.HEX, 0xffff, "Original_timestamp")

local c36 = ProtoField.new("Original_timestamp_tsr", "Original_timestamp", ftypes.UINT32, nil, base.HEX, 0xffff, "Original_timestamp")

local c37 = ProtoField.new("Address_mask_adr_mask", "Address_mask", ftypes.UINT32, nil, base.HEX, 0xffff, "Address_mask")

local c38 = ProtoField.new("Address_mask_addrmask_r", "Address_mask", ftypes.UINT32, nil, base.HEX, 0xffff, "Address_mask")

local c39 = ProtoField.new("ip_header_du", "ip_header", ftypes.UINT32, nil, base.HEX, 0xffff, "ip_header")

local c40 = ProtoField.new("Recieve_timestamp_ts", "Recieve_timestamp", ftypes.UINT32, nil, base.HEX, 0xffff, "Recieve_timestamp")

local c41 = ProtoField.new("Recieve_timestamp_tsr", "Recieve_timestamp", ftypes.UINT32, nil, base.HEX, 0xffff, "Recieve_timestamp")

local c42 = ProtoField.new("Transmit_timestamp_ts", "Transmit_timestamp", ftypes.UINT32, nil, base.HEX, 0xffff, "Transmit_timestamp")

local c43 = ProtoField.new("Transmit_timestamp_tsr", "Transmit_timestamp", ftypes.UINT32, nil, base.HEX, 0xffff, "Transmit_timestamp")

c.fields = { c1, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43}




--------------------------------------------------------------------------------
-- preferences handling stuff
--------------------------------------------------------------------------------

-- a "enum" table for our enum pref, as required by Pref.enum()
-- having the "index" number makes ZERO sense, and is completely illogical
-- but it's what the code has expected it to be for a long time. Ugh.
local debug_pref_enum = {
    { 1,  "Disabled", debug_level.DISABLED },
    { 2,  "Level 1",  debug_level.LEVEL_1  },
    { 3,  "Level 2",  debug_level.LEVEL_2  },
}

c.prefs.debug = Pref.enum("Debug", default_settings.debug_level,
                            "The debug printing level", debug_pref_enum)

c.prefs.port  = Pref.uint("Port number", default_settings.port,
                            "The UDP port number for MyDNS")

c.prefs.heur  = Pref.bool("Heuristic enabled", default_settings.heur_enabled,
                            "Whether heuristic dissection is enabled or not")



function c.dissector(tvbuf, pktinfo, root)

dprint2("dns.dissector called")pktinfo.cols.protocol:set("ICMP_dissector_built")
local offset = 0
local temp = 0
temp = tvbuf:range(offset, 1)
root:add(c1, temp)
if temp == 4 then
temp = tvbuf:range(offset, 1)
root:add(c3, temp)
temp = tvbuf:range(offset, 2)
root:add(c11, temp)
temp = tvbuf:range(offset, 4)
root:add(c19, temp)
temp = tvbuf:range(offset, 4)
root:add(c27, temp)

end
if temp == 5 then
temp = tvbuf:range(offset, 1)
root:add(c4, temp)
temp = tvbuf:range(offset, 2)
root:add(c12, temp)
temp = tvbuf:range(offset, 4)
root:add(c20, temp)

end
if temp == 11 then
temp = tvbuf:range(offset, 1)
root:add(c5, temp)
temp = tvbuf:range(offset, 2)
root:add(c13, temp)
temp = tvbuf:range(offset, 4)
root:add(c21, temp)
temp = tvbuf:range(offset, 4)
root:add(c29, temp)

end
if temp == 13 then
temp = tvbuf:range(offset, 1)
root:add(c6, temp)
temp = tvbuf:range(offset, 2)
root:add(c14, temp)
temp = tvbuf:range(offset, 2)
root:add(c22, temp)
temp = tvbuf:range(offset, 2)
root:add(c30, temp)
temp = tvbuf:range(offset, 4)
root:add(c35, temp)
temp = tvbuf:range(offset, 4)
root:add(c40, temp)
temp = tvbuf:range(offset, 4)
root:add(c42, temp)

end
if temp == 14 then
temp = tvbuf:range(offset, 1)
root:add(c7, temp)
temp = tvbuf:range(offset, 2)
root:add(c15, temp)
temp = tvbuf:range(offset, 2)
root:add(c23, temp)
temp = tvbuf:range(offset, 2)
root:add(c31, temp)
temp = tvbuf:range(offset, 4)
root:add(c36, temp)
temp = tvbuf:range(offset, 4)
root:add(c41, temp)
temp = tvbuf:range(offset, 4)
root:add(c43, temp)

end
if temp == 17 then
temp = tvbuf:range(offset, 1)
root:add(c8, temp)
temp = tvbuf:range(offset, 2)
root:add(c16, temp)
temp = tvbuf:range(offset, 2)
root:add(c24, temp)
temp = tvbuf:range(offset, 2)
root:add(c32, temp)
temp = tvbuf:range(offset, 4)
root:add(c37, temp)

end
if temp == 18 then
temp = tvbuf:range(offset, 1)
root:add(c9, temp)
temp = tvbuf:range(offset, 2)
root:add(c17, temp)
temp = tvbuf:range(offset, 2)
root:add(c25, temp)
temp = tvbuf:range(offset, 2)
root:add(c33, temp)
temp = tvbuf:range(offset, 4)
root:add(c38, temp)

end
if temp == 3 then
temp = tvbuf:range(offset, 1)
root:add(c10, temp)
temp = tvbuf:range(offset, 2)
root:add(c18, temp)
temp = tvbuf:range(offset, 2)
root:add(c26, temp)
temp = tvbuf:range(offset, 2)
root:add(c34, temp)
temp = tvbuf:range(offset, 4)
root:add(c39, temp)

end
return offset
end