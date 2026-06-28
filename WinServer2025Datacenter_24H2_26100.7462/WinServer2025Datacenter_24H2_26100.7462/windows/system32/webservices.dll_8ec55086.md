# Binary Specification: webservices.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\webservices.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8ec55086fbef306b38cf53be62166c70dc20ee3c46c6ef1afdbfb76805da2814`
* **Total Exported Functions:** 193

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 47 | `WsFillReader` | `0x61620` | 33 | UnwindData |  |
| 123 | `WsReadToStartElement` | `0x623C0` | 43 | UnwindData |  |
| 83 | `WsGetReaderNode` | `0x635E0` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `WsReadNode` | `0x63EA0` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `WsWriteStartElement` | `0x64670` | 43 | UnwindData |  |
| 27 | `WsCreateHeap` | `0x66E30` | 53 | UnwindData |  |
| 48 | `WsFindAttribute` | `0x670D0` | 53 | UnwindData |  |
| 32 | `WsCreateReader` | `0x67110` | 33 | UnwindData |  |
| 25 | `WsCreateError` | `0x68E40` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `WsWriteEndElement` | `0x693C0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `WsWriteXmlnsAttribute` | `0x69680` | 43 | UnwindData |  |
| 153 | `WsSetInput` | `0x6A0F0` | 53 | UnwindData |  |
| 37 | `WsCreateWriter` | `0x6AE70` | 33 | UnwindData |  |
| 157 | `WsSetOutput` | `0x6B0C0` | 53 | UnwindData |  |
| 187 | `WsWriteText` | `0x6B1A0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `WsSkipNode` | `0x6B850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `WsSetInputToBuffer` | `0x6B870` | 43 | UnwindData |  |
| 96 | `WsMoveReader` | `0x6B8B0` | 33 | UnwindData |  |
| 122 | `WsReadStartElement` | `0x6BA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `WsGetWriterProperty` | `0x6BA40` | 43 | UnwindData |  |
| 65 | `WsGetErrorProperty` | `0x6BA80` | 33 | UnwindData |  |
| 134 | `WsRequestReply` | `0x6BAB0` | 172 | UnwindData |  |
| 12 | `WsAlloc` | `0x6BB70` | 33 | UnwindData |  |
| 40 | `WsDateTimeToFileTime` | `0x6BBA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `WsFreeReader` | `0x6BD40` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `WsCall` | `0x6BE00` | 94 | UnwindData |  |
| 110 | `WsReadElement` | `0x6C3E0` | 66 | UnwindData |  |
| 53 | `WsFreeHeap` | `0x6C450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `WsWriteStartAttribute` | `0x6C470` | 53 | UnwindData |  |
| 10 | `WsAddMappedHeader` | `0x6CB30` | 66 | UnwindData |  |
| 61 | `WsFreeWriter` | `0x6CB80` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `WsOpenServiceProxy` | `0x6CC30` | 33 | UnwindData |  |
| 38 | `WsCreateXmlBuffer` | `0x6CF30` | 43 | UnwindData |  |
| 36 | `WsCreateServiceProxyFromTemplate` | `0x6D350` | 134 | UnwindData |  |
| 158 | `WsSetOutputToBuffer` | `0x6D3E0` | 43 | UnwindData |  |
| 112 | `WsReadEndElement` | `0x6D970` | 2,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `WsReceiveMessage` | `0x6E310` | 151 | UnwindData |  |
| 193 | `WsXmlStringEquals` | `0x6E7F0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `WsResetHeap` | `0x6EBF0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `WsFreeError` | `0x6ECC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `WsFileTimeToDateTime` | `0x6ECE0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `WsReadType` | `0x6F110` | 120 | UnwindData |  |
| 19 | `WsCloseServiceProxy` | `0x6F440` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `WsReadXmlBufferFromBytes` | `0x6F600` | 122 | UnwindData |  |
| 189 | `WsWriteValue` | `0x6F880` | 43 | UnwindData |  |
| 8 | `WsAddCustomHeader` | `0x6FA10` | 66 | UnwindData |  |
| 173 | `WsWriteElement` | `0x6FA60` | 53 | UnwindData |  |
| 22 | `WsCopyNode` | `0x6FEC0` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `WsStartReaderCanonicalization` | `0x70760` | 53 | UnwindData |  |
| 108 | `WsReadChars` | `0x707A0` | 43 | UnwindData |  |
| 140 | `WsResetMessage` | `0x70A90` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `WsFreeServiceProxy` | `0x70DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `WsSendMessage` | `0x70E10` | 94 | UnwindData |  |
| 35 | `WsCreateServiceProxy` | `0x70E80` | 118 | UnwindData |  |
| 137 | `WsResetError` | `0x70F00` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `WsReadEnvelopeStart` | `0x71160` | 43 | UnwindData |  |
| 174 | `WsWriteEndAttribute` | `0x713E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `WsWriteCharsUtf8` | `0x71400` | 33 | UnwindData |  |
| 93 | `WsInitializeMessage` | `0x71470` | 33 | UnwindData |  |
| 98 | `WsOpenChannel` | `0x71630` | 33 | UnwindData |  |
| 87 | `WsGetSecurityTokenProperty` | `0x717C0` | 53 | UnwindData |  |
| 23 | `WsCreateChannel` | `0x71EC0` | 66 | UnwindData |  |
| 85 | `WsGetReaderProperty` | `0x721C0` | 43 | UnwindData |  |
| 39 | `WsCreateXmlSecurityToken` | `0x722B0` | 53 | UnwindData |  |
| 43 | `WsEndReaderCanonicalization` | `0x722F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `WsCreateMessageForChannel` | `0x72310` | 43 | UnwindData |  |
| 179 | `WsWriteEnvelopeStart` | `0x723A0` | 43 | UnwindData |  |
| 177 | `WsWriteEndStartElement` | `0x72B70` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `WsRemoveMappedHeader` | `0x73610` | 2,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `WsGetChannelProperty` | `0x73E50` | 43 | UnwindData |  |
| 117 | `WsReadMessageStart` | `0x740E0` | 33 | UnwindData |  |
| 84 | `WsGetReaderPosition` | `0x74110` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `WsSetReaderPosition` | `0x74190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WsCloseChannel` | `0x741B0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `WsFreeSecurityToken` | `0x742C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WsMoveWriter` | `0x74310` | 33 | UnwindData |  |
| 55 | `WsFreeMessage` | `0x75110` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `WsGetMappedHeader` | `0x75720` | 134 | UnwindData |  |
| 50 | `WsFlushWriter` | `0x75AD0` | 33 | UnwindData |  |
| 116 | `WsReadMessageEnd` | `0x76710` | 33 | UnwindData |  |
| 168 | `WsWriteAttribute` | `0x772C0` | 53 | UnwindData |  |
| 51 | `WsFreeChannel` | `0x77300` | 4,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `WsWriteBytes` | `0x78340` | 33 | UnwindData |  |
| 178 | `WsWriteEnvelopeEnd` | `0x78600` | 8,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `WsSetWriterPosition` | `0x7A640` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `WsGetWriterPosition` | `0x7A9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `WsReadEnvelopeEnd` | `0x7AA00` | 41,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WsAbandonCall` | `0x84DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WsAbandonMessage` | `0x84E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WsAbortChannel` | `0x84E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WsAbortListener` | `0x84E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WsAbortServiceHost` | `0x84E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WsAbortServiceProxy` | `0x84E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WsAcceptChannel` | `0x84EA0` | 33 | UnwindData |  |
| 9 | `WsAddErrorString` | `0x84ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WsAddressMessage` | `0x84EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WsAsyncExecute` | `0x84F10` | 53 | UnwindData |  |
| 15 | `WsCheckMustUnderstandHeaders` | `0x84F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `WsCloseListener` | `0x84F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `WsCloseServiceHost` | `0x84F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `WsCombineUrl` | `0x84FB0` | 53 | UnwindData |  |
| 21 | `WsCopyError` | `0x84FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WsCreateChannelForListener` | `0x85010` | 43 | UnwindData |  |
| 26 | `WsCreateFaultFromError` | `0x85050` | 43 | UnwindData |  |
| 28 | `WsCreateListener` | `0x85090` | 66 | UnwindData |  |
| 29 | `WsCreateMessage` | `0x850E0` | 53 | UnwindData |  |
| 31 | `WsCreateMetadata` | `0x85120` | 33 | UnwindData |  |
| 33 | `WsCreateServiceEndpointFromTemplate` | `0x85150` | 172 | UnwindData |  |
| 34 | `WsCreateServiceHost` | `0x85210` | 53 | UnwindData |  |
| 41 | `WsDecodeUrl` | `0x85250` | 43 | UnwindData |  |
| 42 | `WsEncodeUrl` | `0x85290` | 43 | UnwindData |  |
| 44 | `WsEndWriterCanonicalization` | `0x852D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `WsFillBody` | `0x852F0` | 33 | UnwindData |  |
| 49 | `WsFlushBody` | `0x85320` | 33 | UnwindData |  |
| 54 | `WsFreeListener` | `0x85350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `WsFreeMetadata` | `0x85370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `WsFreeServiceHost` | `0x85390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `WsGetCustomHeader` | `0x853B0` | 136 | UnwindData |  |
| 64 | `WsGetDictionary` | `0x85440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WsGetErrorString` | `0x85460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `WsGetFaultErrorDetail` | `0x85480` | 53 | UnwindData |  |
| 68 | `WsGetFaultErrorProperty` | `0x854C0` | 33 | UnwindData |  |
| 69 | `WsGetHeader` | `0x854F0` | 94 | UnwindData |  |
| 70 | `WsGetHeaderAttributes` | `0x85560` | 33 | UnwindData |  |
| 71 | `WsGetHeapProperty` | `0x85590` | 43 | UnwindData |  |
| 72 | `WsGetListenerProperty` | `0x855D0` | 43 | UnwindData |  |
| 74 | `WsGetMessageProperty` | `0x85610` | 43 | UnwindData |  |
| 75 | `WsGetMetadataEndpoints` | `0x85650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WsGetMetadataProperty` | `0x85670` | 43 | UnwindData |  |
| 77 | `WsGetMissingMetadataDocumentAddress` | `0x856B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `WsGetNamespaceFromPrefix` | `0x856D0` | 43 | UnwindData |  |
| 79 | `WsGetOperationContextProperty` | `0x85710` | 43 | UnwindData |  |
| 80 | `WsGetPolicyAlternativeCount` | `0x85750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `WsGetPolicyProperty` | `0x85770` | 43 | UnwindData |  |
| 82 | `WsGetPrefixFromNamespace` | `0x857B0` | 43 | UnwindData |  |
| 86 | `WsGetSecurityContextProperty` | `0x857F0` | 43 | UnwindData |  |
| 88 | `WsGetServiceHostProperty` | `0x85830` | 43 | UnwindData |  |
| 89 | `WsGetServiceProxyProperty` | `0x85870` | 43 | UnwindData |  |
| 92 | `WsGetXmlAttribute` | `0x858B0` | 53 | UnwindData |  |
| 94 | `WsMarkHeaderAsUnderstood` | `0x858F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `WsMatchPolicyAlternative` | `0x85910` | 53 | UnwindData |  |
| 99 | `WsOpenListener` | `0x85950` | 33 | UnwindData |  |
| 100 | `WsOpenServiceHost` | `0x85980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WsPullBytes` | `0x859A0` | 33 | UnwindData |  |
| 103 | `WsPushBytes` | `0x859D0` | 33 | UnwindData |  |
| 104 | `WsReadArray` | `0x85A00` | 136 | UnwindData |  |
| 105 | `WsReadAttribute` | `0x85A90` | 66 | UnwindData |  |
| 106 | `WsReadBody` | `0x85AE0` | 66 | UnwindData |  |
| 107 | `WsReadBytes` | `0x85B30` | 43 | UnwindData |  |
| 109 | `WsReadCharsUtf8` | `0x85B70` | 43 | UnwindData |  |
| 111 | `WsReadEndAttribute` | `0x85BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `WsReadEndpointAddressExtension` | `0x85BD0` | 94 | UnwindData |  |
| 118 | `WsReadMetadata` | `0x85C40` | 33 | UnwindData |  |
| 120 | `WsReadQualifiedName` | `0x85C70` | 53 | UnwindData |  |
| 121 | `WsReadStartAttribute` | `0x85CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `WsReadValue` | `0x85CD0` | 43 | UnwindData |  |
| 126 | `WsReadXmlBuffer` | `0x85D10` | 33 | UnwindData |  |
| 129 | `WsRegisterOperationForCancel` | `0x85D40` | 43 | UnwindData |  |
| 130 | `WsRemoveCustomHeader` | `0x85D80` | 33 | UnwindData |  |
| 131 | `WsRemoveHeader` | `0x85DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `WsRemoveNode` | `0x85DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `WsRequestSecurityToken` | `0x85DF0` | 53 | UnwindData |  |
| 136 | `WsResetChannel` | `0x85E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `WsResetListener` | `0x85E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `WsResetMetadata` | `0x85E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `WsResetServiceHost` | `0x85E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `WsResetServiceProxy` | `0x85EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `WsRevokeSecurityContext` | `0x85ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `WsSendFaultMessageForError` | `0x85EF0` | 94 | UnwindData |  |
| 147 | `WsSendReplyMessage` | `0x85F60` | 122 | UnwindData |  |
| 148 | `WsSetChannelProperty` | `0x85FE0` | 43 | UnwindData |  |
| 149 | `WsSetErrorProperty` | `0x86020` | 33 | UnwindData |  |
| 150 | `WsSetFaultErrorDetail` | `0x86050` | 43 | UnwindData |  |
| 151 | `WsSetFaultErrorProperty` | `0x86090` | 33 | UnwindData |  |
| 152 | `WsSetHeader` | `0x860C0` | 66 | UnwindData |  |
| 155 | `WsSetListenerProperty` | `0x86110` | 43 | UnwindData |  |
| 156 | `WsSetMessageProperty` | `0x86150` | 43 | UnwindData |  |
| 161 | `WsShutdownSessionChannel` | `0x86190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `WsStartWriterCanonicalization` | `0x861B0` | 53 | UnwindData |  |
| 165 | `WsTrimXmlWhitespace` | `0x861F0` | 43 | UnwindData |  |
| 166 | `WsVerifyXmlNCName` | `0x86230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `WsWriteArray` | `0x86250` | 122 | UnwindData |  |
| 169 | `WsWriteBody` | `0x862D0` | 53 | UnwindData |  |
| 171 | `WsWriteChars` | `0x86310` | 33 | UnwindData |  |
| 175 | `WsWriteEndCData` | `0x86340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `WsWriteMessageEnd` | `0x86360` | 33 | UnwindData |  |
| 181 | `WsWriteMessageStart` | `0x86390` | 33 | UnwindData |  |
| 182 | `WsWriteNode` | `0x863C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `WsWriteQualifiedName` | `0x863E0` | 43 | UnwindData |  |
| 185 | `WsWriteStartCData` | `0x86420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `WsWriteType` | `0x86440` | 94 | UnwindData |  |
| 190 | `WsWriteXmlBuffer` | `0x864B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `WsWriteXmlBufferToBytes` | `0x864D0` | 120 | UnwindData |  |
