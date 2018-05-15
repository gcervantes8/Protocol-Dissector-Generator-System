# -*- coding: utf-8 -*-
"""
Created on Sat May  13, 9:57:52 2018

@author: Gerardo Cervantes
"""


import StartField
import Field
import EndField
import Expression
import DecisionConstruct
import Protocol
import ReferenceList

def example_ICMP_protocol():
    sf = StartField.StartField('ICMP_dissector_built', 'Example ICMP protocol')
    sf.set_dependency_pattern('1')
    sf.set_dependency_protocol('ip.proto')
#    sf.set_dependency_pattern('Integer')
#    sf.set_dependency_protocol('Dependent protocol')
    
    f1 = Field.Field(1)
    
    sf.set_next_constructs([f1])
    
    f1.set_field_info('ICMP Type', 'Type', 'Checks the type of message', 'ftypes.UINT8', 'base.HEX', 'nil', '?', 'True')
    
    ref_list = ReferenceList.ReferenceList('ref_list')
    ref_list.set_descriptions(['Echo Reply', 'Echo Request'])
    ref_list.set_values(['0', '8'])
    f1.set_ref_list(ref_list)
#    ref_list = ReferenceList.ReferenceList('ref_list')
#    ref_list.set_descriptions(['is a value'])
#    ref_list.set_values(['13'])
#    
#    f1.set_ref_list(ref_list)
    
    source_quench_expr = Expression.Expression()
    source_quench_expr.set_relational_operators_and_operands(['=='], ['4'])
    
    
    redirect_expr = Expression.Expression()
    redirect_expr.set_relational_operators_and_operands(['=='], ['5'])
    
    time_exceeded_expr = Expression.Expression()
    time_exceeded_expr.set_relational_operators_and_operands(['=='], ['11'])
    
    timestamp_expr = Expression.Expression()
    timestamp_expr.set_relational_operators_and_operands(['=='], ['13'])
    
    timestamp_reply_expr = Expression.Expression()
    timestamp_reply_expr.set_relational_operators_and_operands(['=='], ['14'])
    
    addr_mask_req = Expression.Expression()
    addr_mask_req.set_relational_operators_and_operands(['=='], ['17'])
    
    addr_mask_reply_req = Expression.Expression()
    addr_mask_reply_req.set_relational_operators_and_operands(['=='], ['18'])
    
    destination_unreachable = Expression.Expression()
    destination_unreachable.set_relational_operators_and_operands(['=='], ['3'])
    
    otherwise_expr = Expression.Expression()
    otherwise_expr.set_relational_operators_and_operands(['~=', '~=', '~=', '~=', '~=', '~=', '~=', '~='], ['4', '5', '11', '13', '14', '17', '18', '3'])
    otherwise_expr.set_logical_operators(['And', 'And','And', 'And', 'And', 'And', 'And'])
    
    dc = DecisionConstruct.DecisionConstruct()
    dc.set_expressions([source_quench_expr, redirect_expr, time_exceeded_expr, timestamp_expr, timestamp_reply_expr, addr_mask_req, addr_mask_reply_req, destination_unreachable, otherwise_expr])
    f1.set_next_constructs([dc])
    
    source_quench_field = Field.Field(1)
    source_quench_field.set_field_info('Code_source', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    
    source_quench_field_2 = Field.Field(2)
    source_quench_field_2.set_field_info('HeaderChecksum_source', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    source_quench_field_3 = Field.Field(4)
    source_quench_field_3.set_field_info('Unused_source', 'Unused', 'Unused', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    source_quench_field_4 = Field.Field(4)
    source_quench_field_4.set_field_info('IP_header_source', 'IP_header', 'IP_header', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    
    source_quench_field.set_next_constructs([source_quench_field_2])
    source_quench_field_2.set_next_constructs([source_quench_field_3])
    source_quench_field_3.set_next_constructs([source_quench_field_4])
    
    
    redirect_field = Field.Field(1)
    redirect_field.set_field_info('Code_redirect', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    redirect_field_2 = Field.Field(2)
    redirect_field_2.set_field_info('HeaderChecksum_redirect', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    redirect_field_3 = Field.Field(4)
    redirect_field_3.set_field_info('IP_addr_redirect', 'IP_addr', 'IP_addr', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    
    redirect_field.set_next_constructs([redirect_field_2])
    redirect_field_2.set_next_constructs([redirect_field_3])
    
    te_field = Field.Field(1)#Should have reference list
    te_field.set_field_info('Code_te', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    te_field_2 = Field.Field(2)
    te_field_2.set_field_info('HeaderChecksum_te', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    te_field_3 = Field.Field(4)
    te_field_3.set_field_info('Unused_te', 'Unused', 'Unused', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    te_field_4 = Field.Field(4)
    te_field_4.set_field_info('IP_header_te', 'IP_header', 'IP_header', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    
    te_field.set_next_constructs([te_field_2])
    te_field_2.set_next_constructs([te_field_3])
    te_field_3.set_next_constructs([te_field_4])
    
    
    ts_field = Field.Field(1)
    ts_field.set_field_info('Code_ts', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    ts_field_2 = Field.Field(2)
    ts_field_2.set_field_info('HeaderChecksum_ts', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    ts_field_3 = Field.Field(2)
    ts_field_3.set_field_info('Identifier_ts', 'Identifier', 'Identifier', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    ts_field_4 = Field.Field(2)
    ts_field_4.set_field_info('Seq_number_ts', 'Seq_number', 'Seq_number', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    ts_field_5 = Field.Field(4)
    ts_field_5.set_field_info('Original_timestamp_ts', 'Original_timestamp', 'Original_timestamp', 'ftypes.UINT32', 'base.HEX', '0xffff', 'nil', 'True')
    ts_field_6 = Field.Field(4)
    ts_field_6.set_field_info('Recieve_timestamp_ts', 'Recieve_timestamp', 'Recieve_timestamp', 'ftypes.UINT32', 'base.HEX', '0xffff', 'nil', 'True')
    ts_field_7 = Field.Field(4)
    ts_field_7.set_field_info('Transmit_timestamp_ts', 'Transmit_timestamp', 'Transmit_timestamp', 'ftypes.UINT32', 'base.HEX', '0xffff', 'nil', 'True')
    
    ts_field.set_next_constructs([ts_field_2])
    ts_field_2.set_next_constructs([ts_field_3])
    ts_field_3.set_next_constructs([ts_field_4])
    ts_field_4.set_next_constructs([ts_field_5])
    ts_field_5.set_next_constructs([ts_field_6])
    ts_field_6.set_next_constructs([ts_field_7])
    
    
    tsr_field = Field.Field(1)
    tsr_field.set_field_info('Code_tsr_tsr', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    tsr_field_2 = Field.Field(2)
    tsr_field_2.set_field_info('HeaderChecksum_tsr', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    tsr_field_3 = Field.Field(2)
    tsr_field_3.set_field_info('Identifier_tsr', 'Identifier', 'Identifier', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    tsr_field_4 = Field.Field(2)
    tsr_field_4.set_field_info('Seq_number_tsr', 'Seq_number', 'Seq_number', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    tsr_field_5 = Field.Field(4)
    tsr_field_5.set_field_info('Original_timestamp_tsr', 'Original_timestamp', 'Original_timestamp', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    tsr_field_6 = Field.Field(4)
    tsr_field_6.set_field_info('Recieve_timestamp_tsr', 'Recieve_timestamp', 'Recieve_timestamp', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    tsr_field_7 = Field.Field(4)
    tsr_field_7.set_field_info('Transmit_timestamp_tsr', 'Transmit_timestamp', 'Transmit_timestamp', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    
    tsr_field.set_next_constructs([tsr_field_2])
    tsr_field_2.set_next_constructs([tsr_field_3])
    tsr_field_3.set_next_constructs([tsr_field_4])
    tsr_field_4.set_next_constructs([tsr_field_5])
    tsr_field_5.set_next_constructs([tsr_field_6])
    tsr_field_6.set_next_constructs([tsr_field_7])
    
    
    adr_mask_field = Field.Field(1)
    adr_mask_field.set_field_info('Code_addrmask_adr_mask', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    adr_mask_field_2 = Field.Field(2)
    adr_mask_field_2.set_field_info('HeaderChecksum_adr_mask', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    adr_mask_field_3 = Field.Field(2)
    adr_mask_field_3.set_field_info('Identifier_adr_mask', 'Identifier', 'Identifier', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    adr_mask_field_4 = Field.Field(2)
    adr_mask_field_4.set_field_info('Seq_number_adr_mask', 'Seq_number', 'Seq_number', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    adr_mask_field_5 = Field.Field(4)
    adr_mask_field_5.set_field_info('Address_mask_adr_mask', 'Address_mask', 'Address_mask', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')
    
    adr_mask_field.set_next_constructs([adr_mask_field_2])
    adr_mask_field_2.set_next_constructs([adr_mask_field_3])
    adr_mask_field_3.set_next_constructs([adr_mask_field_4])
    adr_mask_field_4.set_next_constructs([adr_mask_field_5])
    

    adr_mask_r_field = Field.Field(1)
    adr_mask_r_field.set_field_info('Code_addrmask_r', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    adr_mask_r_field_2 = Field.Field(2)
    adr_mask_r_field_2.set_field_info('HeaderChecksum_addrmask_r', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    adr_mask_r_field_3 = Field.Field(2)
    adr_mask_r_field_3.set_field_info('Identifier_addrmask_r', 'Identifier', 'Identifier', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    adr_mask_r_field_4 = Field.Field(2)
    adr_mask_r_field_4.set_field_info('Seq_number_addrmask_r', 'Seq_number', 'Seq_number', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    adr_mask_r_field_5 = Field.Field(4)
    adr_mask_r_field_5.set_field_info('Address_mask_addrmask_r', 'Address_mask', 'Address_mask', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')

    adr_mask_r_field.set_next_constructs([adr_mask_r_field_2])
    adr_mask_r_field_2.set_next_constructs([adr_mask_r_field_3])
    adr_mask_r_field_3.set_next_constructs([adr_mask_r_field_4])
    adr_mask_r_field_4.set_next_constructs([adr_mask_r_field_5])

    du_field = Field.Field(1)
    du_field.set_field_info('Code_du', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    du_field_2 = Field.Field(2)
    du_field_2.set_field_info('HeaderChecksum_du', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    du_field_3 = Field.Field(2)
    du_field_3.set_field_info('Unused_du', 'Unused', 'Unused', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    du_field_4 = Field.Field(2)
    du_field_4.set_field_info('Next_hop_MTU_du', 'Next_hop_MTU', 'Next_hop_MTU', 'ftypes.UINT16', 'nil', '0xff', 'nil', 'True')
    du_field_5 = Field.Field(4)
    du_field_5.set_field_info('ip_header_du', 'ip_header', 'ip_header', 'ftypes.UINT32', 'nil', '0xffff', 'nil', 'True')

    
    du_field.set_next_constructs([du_field_2])
    du_field_2.set_next_constructs([du_field_3])
    du_field_3.set_next_constructs([du_field_4])
    du_field_4.set_next_constructs([du_field_5])
    
    other_field = Field.Field(1)
    other_field.set_field_info('Code_Other', 'Code', 'Code', 'ftypes.UINT8', 'nil', '0xf', 'nil', 'True')
    other_field_2 = Field.Field(2)
    other_field_2.set_field_info('HeaderChecksum_other', 'HeaderChecksum', 'HeaderChecksum', 'ftypes.UINT16', 'base.HEX', '0xff', 'nil', 'True')
    
    other_field.set_next_constructs([other_field_2])
    
    
    dc.set_next_constructs([source_quench_field, redirect_field, te_field, ts_field, tsr_field, adr_mask_field, adr_mask_r_field, du_field, other_field])
    end_field = EndField.EndField()
    
    source_quench_field_4.set_next_constructs([end_field])
    redirect_field_3.set_next_constructs([end_field])
    te_field_4.set_next_constructs([end_field])
    ts_field_7.set_next_constructs([end_field])
    tsr_field_7.set_next_constructs([end_field])
    adr_mask_field_5.set_next_constructs([end_field])
    adr_mask_r_field_5.set_next_constructs([end_field])
    du_field_5.set_next_constructs([end_field])
    other_field_2.set_next_constructs([end_field])
    
    
    protocol = Protocol.Protocol()
    protocol_structure = protocol.get_protocol_structure(sf)
    return protocol_structure


if __name__ == "__main__":
    protocol_struct = example_ICMP_protocol()
    p_file = open('icmp_xml_intermediate.xml','w')
    p_file.write(protocol_struct)
    p_file.close()
#    print(protocol_struct)