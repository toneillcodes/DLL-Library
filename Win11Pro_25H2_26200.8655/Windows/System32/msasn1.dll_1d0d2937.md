# Binary Specification: msasn1.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msasn1.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1d0d2937c28f5cf8bc8c49a0e1f32703edf557d8735cdd273c171417d921e535`
* **Total Exported Functions:** 152

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `ASN1BERDecOctetString` | `0x1490` | 36 | UnwindData |  |
| 35 | `ASN1BERDecUTF8String` | `0x14C0` | 574 | UnwindData |  |
| 21 | `ASN1BERDecOctetString2` | `0x1710` | 39 | UnwindData |  |
| 6 | `ASN1BERDecCharString` | `0x1CB0` | 1,118 | UnwindData |  |
| 23 | `ASN1BERDecOpenType2` | `0x2650` | 1,156 | UnwindData |  |
| 9 | `ASN1BERDecEndOfContents` | `0x2AE0` | 235 | UnwindData |  |
| 32 | `ASN1BERDecU32Val` | `0x2BE0` | 858 | UnwindData |  |
| 7 | `ASN1BERDecCheck` | `0x2F40` | 42 | UnwindData |  |
| 11 | `ASN1BERDecExplicitTag` | `0x2F70` | 887 | UnwindData |  |
| 31 | `ASN1BERDecU16Val` | `0x32F0` | 198 | UnwindData |  |
| 17 | `ASN1BERDecNull` | `0x33C0` | 84 | UnwindData |  |
| 18 | `ASN1BERDecObjectIdentifier` | `0x3420` | 441 | UnwindData |  |
| 14 | `ASN1BERDecLength` | `0x35E0` | 368 | UnwindData |  |
| 30 | `ASN1BERDecTag` | `0x3760` | 265 | UnwindData |  |
| 69 | `ASN1BEREoid2DotVal` | `0x38E0` | 667 | UnwindData |  |
| 12 | `ASN1BERDecFlush` | `0x3C10` | 41 | UnwindData |  |
| 100 | `ASN1DecSetError` | `0x3C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ASN1BERDecEoid` | `0x3C70` | 762 | UnwindData |  |
| 16 | `ASN1BERDecNotEndOfContents` | `0x3F70` | 75 | UnwindData |  |
| 111 | `ASN1_Decode` | `0x4130` | 680 | UnwindData |  |
| 113 | `ASN1_FreeDecoded` | `0x43E0` | 99 | UnwindData |  |
| 103 | `ASN1_CloseDecoder` | `0x4450` | 81 | UnwindData |  |
| 28 | `ASN1BERDecSXVal` | `0x44B0` | 726 | UnwindData |  |
| 29 | `ASN1BERDecSkip` | `0x4790` | 259 | UnwindData |  |
| 13 | `ASN1BERDecGeneralizedTime` | `0x48A0` | 166 | UnwindData |  |
| 34 | `ASN1BERDecUTCTime` | `0x4950` | 42 | UnwindData |  |
| 38 | `ASN1BERDecZeroCharString` | `0x4A20` | 1,192 | UnwindData |  |
| 19 | `ASN1BERDecObjectIdentifier2` | `0x5670` | 943 | UnwindData |  |
| 26 | `ASN1BERDecS32Val` | `0x5A30` | 832 | UnwindData |  |
| 24 | `ASN1BERDecPeekTag` | `0x5D80` | 41 | UnwindData |  |
| 108 | `ASN1_CreateDecoderEx` | `0x5E80` | 362 | UnwindData |  |
| 107 | `ASN1_CreateDecoder` | `0x5FF0` | 295 | UnwindData |  |
| 67 | `ASN1BEREncUTF8String` | `0x6120` | 301 | UnwindData |  |
| 91 | `ASN1DEREncGeneralizedTime` | `0x6260` | 122 | UnwindData |  |
| 40 | `ASN1BERDotVal2Eoid` | `0x62E0` | 513 | UnwindData |  |
| 42 | `ASN1BEREncBool` | `0x6580` | 78 | UnwindData |  |
| 95 | `ASN1DEREncUTCTime` | `0x65E0` | 116 | UnwindData |  |
| 65 | `ASN1BEREncU32` | `0x6660` | 199 | UnwindData |  |
| 41 | `ASN1BEREncBitString` | `0x6730` | 187 | UnwindData |  |
| 62 | `ASN1BEREncS32` | `0x6800` | 247 | UnwindData |  |
| 43 | `ASN1BEREncChar16String` | `0x6900` | 135 | UnwindData |  |
| 63 | `ASN1BEREncSX` | `0x6990` | 131 | UnwindData |  |
| 45 | `ASN1BEREncCharString` | `0x6A20` | 92 | UnwindData |  |
| 58 | `ASN1BEREncOctetString` | `0x6A20` | 92 | UnwindData |  |
| 49 | `ASN1BEREncEoid` | `0x6A90` | 94 | UnwindData |  |
| 48 | `ASN1BEREncEndOfContents` | `0x6B00` | 148 | UnwindData |  |
| 56 | `ASN1BEREncObjectIdentifier` | `0x6C60` | 281 | UnwindData |  |
| 57 | `ASN1BEREncObjectIdentifier2` | `0x6E30` | 439 | UnwindData |  |
| 89 | `ASN1DEREncEndBlk` | `0x6FF0` | 277 | UnwindData |  |
| 104 | `ASN1_CloseEncoder` | `0x7110` | 41 | UnwindData |  |
| 93 | `ASN1DEREncNewBlkElement` | `0x7140` | 215 | UnwindData |  |
| 109 | `ASN1_CreateEncoder` | `0x7220` | 55 | UnwindData |  |
| 59 | `ASN1BEREncOpenType` | `0x7370` | 70 | UnwindData |  |
| 53 | `ASN1BEREncLength` | `0x73C0` | 187 | UnwindData |  |
| 50 | `ASN1BEREncExplicitTag` | `0x7490` | 79 | UnwindData |  |
| 64 | `ASN1BEREncTag` | `0x74F0` | 260 | UnwindData |  |
| 112 | `ASN1_Encode` | `0x7760` | 436 | UnwindData |  |
| 90 | `ASN1DEREncFlushBlkElement` | `0x7920` | 367 | UnwindData |  |
| 51 | `ASN1BEREncFlush` | `0x7AA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `ASN1EncSetError` | `0x7AE0` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `ASN1DecRealloc` | `0x82D0` | 133 | UnwindData |  |
| 4 | `ASN1BERDecChar16String` | `0x8360` | 1,188 | UnwindData |  |
| 3 | `ASN1BERDecBool` | `0x8810` | 608 | UnwindData |  |
| 70 | `ASN1BEREoid_free` | `0x8A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `ASN1charstring_free` | `0x8A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `ASN1bitstring_free` | `0x8AA0` | 31 | UnwindData |  |
| 122 | `ASN1char16string_free` | `0x8AA0` | 31 | UnwindData |  |
| 124 | `ASN1char32string_free` | `0x8AA0` | 31 | UnwindData |  |
| 132 | `ASN1intx_free` | `0x8AA0` | 31 | UnwindData |  |
| 141 | `ASN1octetstring_free` | `0x8AA0` | 31 | UnwindData |  |
| 143 | `ASN1open_free` | `0x8AA0` | 31 | UnwindData |  |
| 146 | `ASN1utf8string_free` | `0x8AA0` | 31 | UnwindData |  |
| 84 | `ASN1DEREncBeginBlk` | `0x8AD0` | 158 | UnwindData |  |
| 118 | `ASN1_SetEncoderOption` | `0x8B80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ASN1BERDecBitString2` | `0x8C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ASN1_FreeEncoded` | `0x8C30` | 30 | UnwindData |  |
| 102 | `ASN1Free` | `0x8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `ASN1_CloseModule` | `0x8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `ASN1ztchar16string_free` | `0x8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `ASN1ztchar32string_free` | `0x8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `ASN1ztcharstring_free` | `0x8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `ASN1_CreateModule` | `0x8C80` | 214 | UnwindData |  |
| 119 | `ASN1bitstring_cmp` | `0x8EA0` | 223 | UnwindData |  |
| 61 | `ASN1BEREncRemoveZeroBits2` | `0x8F90` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `ASN1BEREncCheck` | `0x9040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ASN1BERDecOpenType` | `0x9050` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `ASN1objectidentifier_free` | `0x90B0` | 30 | UnwindData |  |
| 60 | `ASN1BEREncRemoveZeroBits` | `0x90E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `ASN1DEREncCharString` | `0x9180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `ASN1DEREncOctetString` | `0x9180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ASN1BERDecBitString` | `0x9190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `ASN1intx_setuint32` | `0x91A0` | 184 | UnwindData |  |
| 15 | `ASN1BERDecMultibyteString` | `0x9260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ASN1DEREncBitString` | `0x9270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `ASN1DecAlloc` | `0x9280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `ASN1intxisuint32` | `0x9290` | 38 | UnwindData |  |
| 129 | `ASN1intx2uint32` | `0x92C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ASN1DEREncChar16String` | `0x9350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `ASN1intx_uoctets` | `0x9360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `ASN1DEREncUTF8String` | `0x9390` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ASN1BERDecChar32String` | `0x97A0` | 613 | UnwindData |  |
| 25 | `ASN1BERDecS16Val` | `0x9A10` | 153 | UnwindData |  |
| 27 | `ASN1BERDecS8Val` | `0x9AB0` | 111 | UnwindData |  |
| 33 | `ASN1BERDecU8Val` | `0x9B30` | 148 | UnwindData |  |
| 36 | `ASN1BERDecZeroChar16String` | `0x9BD0` | 22 | UnwindData |  |
| 37 | `ASN1BERDecZeroChar32String` | `0x9BD0` | 22 | UnwindData |  |
| 39 | `ASN1BERDecZeroMultibyteString` | `0x9BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ASN1BEREncChar32String` | `0x9C00` | 163 | UnwindData |  |
| 52 | `ASN1BEREncGeneralizedTime` | `0x9CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `ASN1CEREncGeneralizedTime` | `0x9CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ASN1BEREncMultibyteString` | `0x9CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `ASN1DEREncMultibyteString` | `0x9CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ASN1BEREncNull` | `0x9CE0` | 42 | UnwindData |  |
| 66 | `ASN1BEREncUTCTime` | `0x9D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `ASN1CEREncUTCTime` | `0x9D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `ASN1BEREncZeroMultibyteString` | `0x9D20` | 76 | UnwindData |  |
| 121 | `ASN1char16string_cmp` | `0x9D80` | 88 | UnwindData |  |
| 123 | `ASN1char32string_cmp` | `0x9DE0` | 85 | UnwindData |  |
| 125 | `ASN1charstring_cmp` | `0x9E40` | 87 | UnwindData |  |
| 127 | `ASN1generalizedtime_cmp` | `0x9EA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `ASN1intx_cmp` | `0x9F30` | 206 | UnwindData |  |
| 137 | `ASN1objectidentifier2_cmp` | `0xA010` | 82 | UnwindData |  |
| 138 | `ASN1objectidentifier_cmp` | `0xA070` | 86 | UnwindData |  |
| 140 | `ASN1octetstring_cmp` | `0xA0D0` | 51 | UnwindData |  |
| 142 | `ASN1open_cmp` | `0xA110` | 72 | UnwindData |  |
| 145 | `ASN1utctime_cmp` | `0xA160` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `ASN1ztchar16string_cmp` | `0xA1E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `ASN1ztchar32string_cmp` | `0xA210` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `ASN1ztcharstring_cmp` | `0xA250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ASN1BERDecDouble` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ASN1BEREncDouble` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ASN1CEREncBitString` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `ASN1CEREncChar16String` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ASN1CEREncChar32String` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ASN1CEREncCharString` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ASN1CEREncMultibyteString` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ASN1CEREncOctetString` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ASN1CEREncZeroMultibyteString` | `0xA280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `ASN1intx_add` | `0xA290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `ASN1intx_sub` | `0xA290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `ASN1intx2int32` | `0xA2A0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `ASN1uint32_uoctets` | `0xA370` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ASN1CEREncBeginBlk` | `0xA3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `ASN1CEREncEndBlk` | `0xA3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `ASN1CEREncFlushBlkElement` | `0xA3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `ASN1CEREncNewBlkElement` | `0xA3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `ASN1DEREncChar32String` | `0xA3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `ASN1DEREncZeroMultibyteString` | `0xA3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `ASN1_CloseEncoder2` | `0xA400` | 44 | UnwindData |  |
| 115 | `ASN1_GetDecoderOption` | `0xA440` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `ASN1_GetEncoderOption` | `0xA480` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `ASN1_SetDecoderOption` | `0xA4C0` | 0 | Indeterminate |  |
