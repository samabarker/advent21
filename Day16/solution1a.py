hex_bin = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}

input_hex = "005473C9244483004B001F79A9CE75FF9065446725685F1223600542661B7A9F4D001428C01D8C30C61210021F0663043A20042616C75868800BAC9CB59F4BC3A40232680220008542D89B114401886F1EA2DCF16CFE3BE6281060104B00C9994B83C13200AD3C0169B85FA7D3BE0A91356004824A32E6C94803A1D005E6701B2B49D76A1257EC7310C2015E7C0151006E0843F8D000086C4284910A47518CF7DD04380553C2F2D4BFEE67350DE2C9331FEFAFAD24CB282004F328C73F4E8B49C34AF094802B2B004E76762F9D9D8BA500653EEA4016CD802126B72D8F004C5F9975200C924B5065C00686467E58919F960C017F00466BB3B6B4B135D9DB5A5A93C2210050B32A9400A9497D524BEA660084EEA8EF600849E21EFB7C9F07E5C34C014C009067794BCC527794BCC424F12A67DCBC905C01B97BF8DE5ED9F7C865A4051F50024F9B9EAFA93ECE1A49A2C2E20128E4CA30037100042612C6F8B600084C1C8850BC400B8DAA01547197D6370BC8422C4A72051291E2A0803B0E2094D4BB5FDBEF6A0094F3CCC9A0002FD38E1350E7500C01A1006E3CC24884200C46389312C401F8551C63D4CC9D08035293FD6FCAFF1468B0056780A45D0C01498FBED0039925B82CCDCA7F4E20021A692CC012B00440010B8691761E0002190E21244C98EE0B0C0139297660B401A80002150E20A43C1006A0E44582A400C04A81CD994B9A1004BB1625D0648CE440E49DC402D8612BB6C9F5E97A5AC193F589A100505800ABCF5205138BD2EB527EA130008611167331AEA9B8BDCC4752B78165B39DAA1004C906740139EB0148D3CEC80662B801E60041015EE6006801364E007B801C003F1A801880350100BEC002A3000920E0079801CA00500046A800C0A001A73DFE9830059D29B5E8A51865777DCA1A2820040E4C7A49F88028B9F92DF80292E592B6B840"
input_bin = "" 
for item in input_hex:
    input_bin += hex_bin[item]
print(input_bin)

packet_versions = []


def RunCode(start):
    packet_version = int(input_bin[start:start+3],2)
    packet_id = int(input_bin[start+3:start+6],2)
    packet_versions.append(packet_version)
    if packet_id == 4:
        literal = ''
        counter = 0
        while True:
            if input_bin[start+6+counter] == '0':
                literal += input_bin[start+6+counter:start+6+counter+5]
                counter += 5
                break
            else:
                literal += input_bin[start+6+counter:start+6+counter+5]
                counter += 5
        return(counter+6)
    else:
        length_id = input_bin[start+6]
        if length_id == '0':
            number_of_bits = int(input_bin[start+7:start+7+15],2)
            counter = 0
            while counter < number_of_bits:
                counter += RunCode(start+7+15+counter)
            return(7+15+counter)
        else:
            number_of_subpackets = int(input_bin[start+7:start+7+11],2)
            counter = 0
            num_of_subs = 0
            while num_of_subs < number_of_subpackets:
                counter += RunCode(start+7+11+counter)
                num_of_subs += 1
            return(7+11+counter)
    return 0

RunCode(0)
print(sum(packet_versions))