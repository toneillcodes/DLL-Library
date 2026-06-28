# Binary Specification: tapi32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tapi32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `349c27b052ba17571737e81c0d70e9a80249ae9c981a7d1aa1dcc26360fe64f4`
* **Total Exported Functions:** 278

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetTapi16CallbackMsg` | `0x55B0` | 213 | UnwindData |  |
| 2 | `LAddrParamsInited` | `0x5A40` | 252 | UnwindData |  |
| 3 | `LOpenDialAsst` | `0x5B50` | 260 | UnwindData |  |
| 21 | `NonAsyncEventThread` | `0x5F90` | 27 | UnwindData |  |
| 22 | `TAPIWndProc` | `0x60F0` | 681 | UnwindData |  |
| 23 | `TUISPIDLLCallback` | `0x63A0` | 144 | UnwindData |  |
| 27 | `internalPerformance` | `0x6AF0` | 117 | UnwindData |  |
| 30 | `lineAccept` | `0x6B70` | 156 | UnwindData |  |
| 31 | `lineAddProvider` | `0x6C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `lineAddProviderA` | `0x6C30` | 230 | UnwindData |  |
| 33 | `lineAddProviderW` | `0x6D20` | 333 | UnwindData |  |
| 34 | `lineAddToConference` | `0x6E80` | 116 | UnwindData |  |
| 35 | `lineAgentSpecific` | `0x6F00` | 255 | UnwindData |  |
| 36 | `lineAnswer` | `0x7010` | 156 | UnwindData |  |
| 37 | `lineBlindTransfer` | `0x70C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `lineBlindTransferA` | `0x70D0` | 167 | UnwindData |  |
| 39 | `lineBlindTransferW` | `0x7180` | 180 | UnwindData |  |
| 40 | `lineClose` | `0x7240` | 159 | UnwindData |  |
| 41 | `lineCompleteCall` | `0x72F0` | 241 | UnwindData |  |
| 42 | `lineCompleteTransfer` | `0x74A0` | 250 | UnwindData |  |
| 43 | `lineConfigDialog` | `0x75A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `lineConfigDialogA` | `0x75B0` | 123 | UnwindData |  |
| 45 | `lineConfigDialogEdit` | `0x7640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `lineConfigDialogEditA` | `0x7650` | 157 | UnwindData |  |
| 47 | `lineConfigDialogEditW` | `0x7700` | 343 | UnwindData |  |
| 48 | `lineConfigDialogW` | `0x7860` | 210 | UnwindData |  |
| 49 | `lineConfigProvider` | `0x7940` | 36 | UnwindData |  |
| 50 | `lineCreateAgentA` | `0x7970` | 216 | UnwindData |  |
| 51 | `lineCreateAgentSessionA` | `0x7A50` | 161 | UnwindData |  |
| 52 | `lineCreateAgentSessionW` | `0x7B00` | 319 | UnwindData |  |
| 53 | `lineCreateAgentW` | `0x7C50` | 332 | UnwindData |  |
| 54 | `lineDeallocateCall` | `0x7DB0` | 172 | UnwindData |  |
| 55 | `lineDevSpecific` | `0x7E70` | 259 | UnwindData |  |
| 56 | `lineDevSpecificFeature` | `0x7F80` | 250 | UnwindData |  |
| 57 | `lineDial` | `0x81A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `lineDialA` | `0x81B0` | 154 | UnwindData |  |
| 59 | `lineDialW` | `0x8250` | 177 | UnwindData |  |
| 60 | `lineDrop` | `0x8310` | 156 | UnwindData |  |
| 61 | `lineForward` | `0x83C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `lineForwardA` | `0x83D0` | 324 | UnwindData |  |
| 63 | `lineForwardW` | `0x8520` | 310 | UnwindData |  |
| 64 | `lineGatherDigits` | `0x8660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `lineGatherDigitsA` | `0x8670` | 396 | UnwindData |  |
| 66 | `lineGatherDigitsW` | `0x8900` | 327 | UnwindData |  |
| 67 | `lineGenerateDigits` | `0x8B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `lineGenerateDigitsA` | `0x8B20` | 241 | UnwindData |  |
| 69 | `lineGenerateDigitsW` | `0x8C20` | 156 | UnwindData |  |
| 70 | `lineGenerateTone` | `0x8CD0` | 171 | UnwindData |  |
| 71 | `lineGetAddressCaps` | `0x8D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `lineGetAddressCapsA` | `0x8DA0` | 416 | UnwindData |  |
| 73 | `lineGetAddressCapsW` | `0x8F50` | 170 | UnwindData |  |
| 74 | `lineGetAddressID` | `0x9000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `lineGetAddressIDA` | `0x9010` | 291 | UnwindData |  |
| 76 | `lineGetAddressIDW` | `0x9140` | 134 | UnwindData |  |
| 77 | `lineGetAddressStatus` | `0x91D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `lineGetAddressStatusA` | `0x91E0` | 207 | UnwindData |  |
| 79 | `lineGetAddressStatusW` | `0x92C0` | 119 | UnwindData |  |
| 80 | `lineGetAgentActivityListA` | `0x9340` | 217 | UnwindData |  |
| 81 | `lineGetAgentActivityListW` | `0x95D0` | 244 | UnwindData |  |
| 82 | `lineGetAgentCapsA` | `0x96D0` | 235 | UnwindData |  |
| 83 | `lineGetAgentCapsW` | `0x9900` | 263 | UnwindData |  |
| 84 | `lineGetAgentGroupListA` | `0x9A10` | 217 | UnwindData |  |
| 85 | `lineGetAgentGroupListW` | `0x9CA0` | 244 | UnwindData |  |
| 86 | `lineGetAgentInfo` | `0x9DA0` | 244 | UnwindData |  |
| 87 | `lineGetAgentSessionInfo` | `0x9EA0` | 244 | UnwindData |  |
| 88 | `lineGetAgentSessionList` | `0x9FA0` | 244 | UnwindData |  |
| 89 | `lineGetAgentStatusA` | `0xA0A0` | 205 | UnwindData |  |
| 90 | `lineGetAgentStatusW` | `0xA340` | 244 | UnwindData |  |
| 91 | `lineGetAppPriority` | `0xA440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `lineGetAppPriorityA` | `0xA450` | 300 | UnwindData |  |
| 93 | `lineGetAppPriorityW` | `0xA590` | 251 | UnwindData |  |
| 94 | `lineGetCallInfo` | `0xA6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `lineGetCallInfoA` | `0xA6B0` | 246 | UnwindData |  |
| 96 | `lineGetCallInfoW` | `0xA7B0` | 115 | UnwindData |  |
| 97 | `lineGetCallStatus` | `0xA830` | 115 | UnwindData |  |
| 98 | `lineGetConfRelatedCalls` | `0xA8B0` | 115 | UnwindData |  |
| 99 | `lineGetCountry` | `0xA930` | 687 | UnwindData |  |
| 100 | `lineGetCountryA` | `0xABF0` | 187 | UnwindData |  |
| 101 | `lineGetCountryW` | `0xACC0` | 180 | UnwindData |  |
| 102 | `lineGetDevCaps` | `0xAD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `lineGetDevCapsA` | `0xAD90` | 157 | UnwindData |  |
| 104 | `lineGetDevCapsW` | `0xAE40` | 170 | UnwindData |  |
| 105 | `lineGetDevConfig` | `0xAEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `lineGetDevConfigA` | `0xAF00` | 204 | UnwindData |  |
| 107 | `lineGetDevConfigW` | `0xAFE0` | 179 | UnwindData |  |
| 108 | `lineGetGroupListA` | `0xB0A0` | 199 | UnwindData |  |
| 109 | `lineGetGroupListW` | `0xB170` | 238 | UnwindData |  |
| 110 | `lineGetID` | `0xB270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `lineGetIDA` | `0xB280` | 221 | UnwindData |  |
| 112 | `lineGetIDW` | `0xB370` | 964 | UnwindData |  |
| 113 | `lineGetIcon` | `0xB740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `lineGetIconA` | `0xB750` | 122 | UnwindData |  |
| 115 | `lineGetIconW` | `0xB7D0` | 185 | UnwindData |  |
| 116 | `lineGetLineDevStatus` | `0xB890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `lineGetLineDevStatusA` | `0xB8A0` | 309 | UnwindData |  |
| 118 | `lineGetLineDevStatusW` | `0xB9E0` | 115 | UnwindData |  |
| 119 | `lineGetMessage` | `0xBA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `lineGetNewCalls` | `0xBA80` | 121 | UnwindData |  |
| 121 | `lineGetNumRings` | `0xBB00` | 119 | UnwindData |  |
| 122 | `lineGetProviderList` | `0xBB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `lineGetProviderListA` | `0xBB90` | 155 | UnwindData |  |
| 124 | `lineGetProviderListW` | `0xBC40` | 241 | UnwindData |  |
| 125 | `lineGetProxyStatus` | `0xBD40` | 138 | UnwindData |  |
| 126 | `lineGetQueueInfo` | `0xBDD0` | 244 | UnwindData |  |
| 127 | `lineGetQueueListA` | `0xBED0` | 224 | UnwindData |  |
| 128 | `lineGetQueueListW` | `0xC170` | 263 | UnwindData |  |
| 129 | `lineGetRequest` | `0xC280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `lineGetRequestA` | `0xC290` | 598 | UnwindData |  |
| 131 | `lineGetRequestW` | `0xC4F0` | 166 | UnwindData |  |
| 132 | `lineGetStatusMessages` | `0xC5A0` | 140 | UnwindData |  |
| 136 | `lineHandoff` | `0xC640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `lineHandoffA` | `0xC650` | 136 | UnwindData |  |
| 138 | `lineHandoffW` | `0xC6E0` | 154 | UnwindData |  |
| 139 | `lineHold` | `0xC780` | 108 | UnwindData |  |
| 140 | `lineInitialize` | `0xC800` | 174 | UnwindData |  |
| 141 | `lineInitializeExA` | `0xC8C0` | 188 | UnwindData |  |
| 142 | `lineInitializeExW` | `0xC990` | 161 | UnwindData |  |
| 143 | `lineMakeCall` | `0xCA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `lineMakeCallA` | `0xCA50` | 429 | UnwindData |  |
| 145 | `lineMakeCallW` | `0xCCC0` | 292 | UnwindData |  |
| 146 | `lineMonitorDigits` | `0xCDF0` | 116 | UnwindData |  |
| 147 | `lineMonitorMedia` | `0xCE70` | 116 | UnwindData |  |
| 148 | `lineMonitorTones` | `0xCEF0` | 168 | UnwindData |  |
| 149 | `lineNegotiateAPIVersion` | `0xCFA0` | 184 | UnwindData |  |
| 150 | `lineNegotiateExtVersion` | `0xD060` | 170 | UnwindData |  |
| 151 | `lineOpen` | `0xD110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `lineOpenA` | `0xD120` | 430 | UnwindData |  |
| 153 | `lineOpenW` | `0xD2E0` | 416 | UnwindData |  |
| 154 | `linePark` | `0xD490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `lineParkA` | `0xD4A0` | 360 | UnwindData |  |
| 156 | `lineParkW` | `0xD820` | 296 | UnwindData |  |
| 157 | `linePickup` | `0xD950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `linePickupA` | `0xD960` | 221 | UnwindData |  |
| 159 | `linePickupW` | `0xDA50` | 286 | UnwindData |  |
| 160 | `linePrepareAddToConference` | `0xDB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `linePrepareAddToConferenceA` | `0xDB90` | 277 | UnwindData |  |
| 162 | `linePrepareAddToConferenceW` | `0xDCB0` | 258 | UnwindData |  |
| 163 | `lineProxyMessage` | `0xDDC0` | 147 | UnwindData |  |
| 164 | `lineProxyResponse` | `0xDE60` | 329 | UnwindData |  |
| 165 | `lineRedirect` | `0xDFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `lineRedirectA` | `0xDFC0` | 128 | UnwindData |  |
| 167 | `lineRedirectW` | `0xE050` | 121 | UnwindData |  |
| 168 | `lineRegisterRequestRecipient` | `0xE0D0` | 124 | UnwindData |  |
| 169 | `lineReleaseUserUserInfo` | `0xE160` | 108 | UnwindData |  |
| 170 | `lineRemoveFromConference` | `0xE1E0` | 108 | UnwindData |  |
| 171 | `lineRemoveProvider` | `0xE260` | 36 | UnwindData |  |
| 172 | `lineSecureCall` | `0xE290` | 108 | UnwindData |  |
| 173 | `lineSendUserUserInfo` | `0xE310` | 156 | UnwindData |  |
| 174 | `lineSetAgentActivity` | `0xE3C0` | 120 | UnwindData |  |
| 175 | `lineSetAgentGroup` | `0xE440` | 153 | UnwindData |  |
| 176 | `lineSetAgentMeasurementPeriod` | `0xE4E0` | 120 | UnwindData |  |
| 177 | `lineSetAgentSessionState` | `0xE560` | 120 | UnwindData |  |
| 178 | `lineSetAgentState` | `0xE5E0` | 120 | UnwindData |  |
| 179 | `lineSetAgentStateEx` | `0xE660` | 120 | UnwindData |  |
| 180 | `lineSetAppPriority` | `0xE6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `lineSetAppPriorityA` | `0xE6F0` | 113 | UnwindData |  |
| 182 | `lineSetAppPriorityW` | `0xE770` | 148 | UnwindData |  |
| 183 | `lineSetAppSpecific` | `0xE810` | 116 | UnwindData |  |
| 184 | `lineSetCallData` | `0xE890` | 152 | UnwindData |  |
| 185 | `lineSetCallParams` | `0xE930` | 171 | UnwindData |  |
| 186 | `lineSetCallPrivilege` | `0xE9F0` | 116 | UnwindData |  |
| 187 | `lineSetCallQualityOfService` | `0xEA70` | 134 | UnwindData |  |
| 188 | `lineSetCallTreatment` | `0xEB00` | 116 | UnwindData |  |
| 190 | `lineSetDevConfig` | `0xEB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `lineSetDevConfigA` | `0xEB90` | 151 | UnwindData |  |
| 192 | `lineSetDevConfigW` | `0xEC30` | 119 | UnwindData |  |
| 193 | `lineSetLineDevStatus` | `0xECB0` | 120 | UnwindData |  |
| 194 | `lineSetMediaControl` | `0xED30` | 304 | UnwindData |  |
| 195 | `lineSetMediaMode` | `0xEE70` | 116 | UnwindData |  |
| 196 | `lineSetNumRings` | `0xEEF0` | 120 | UnwindData |  |
| 197 | `lineSetQueueMeasurementPeriod` | `0xEF70` | 120 | UnwindData |  |
| 198 | `lineSetStatusMessages` | `0xEFF0` | 120 | UnwindData |  |
| 199 | `lineSetTerminal` | `0xF070` | 148 | UnwindData |  |
| 203 | `lineSetupConference` | `0xF110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `lineSetupConferenceA` | `0xF120` | 358 | UnwindData |  |
| 205 | `lineSetupConferenceW` | `0xF360` | 344 | UnwindData |  |
| 206 | `lineSetupTransfer` | `0xF4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `lineSetupTransferA` | `0xF4D0` | 277 | UnwindData |  |
| 208 | `lineSetupTransferW` | `0xF5F0` | 258 | UnwindData |  |
| 209 | `lineShutdown` | `0xF700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `lineSwapHold` | `0xF710` | 116 | UnwindData |  |
| 217 | `lineUncompleteCall` | `0xF790` | 116 | UnwindData |  |
| 218 | `lineUnhold` | `0xF810` | 108 | UnwindData |  |
| 219 | `lineUnpark` | `0xF890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `lineUnparkA` | `0xF8A0` | 149 | UnwindData |  |
| 221 | `lineUnparkW` | `0xF940` | 240 | UnwindData |  |
| 222 | `phoneClose` | `0xFE40` | 159 | UnwindData |  |
| 223 | `phoneConfigDialog` | `0xFEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `phoneConfigDialogA` | `0xFF00` | 123 | UnwindData |  |
| 225 | `phoneConfigDialogW` | `0xFF90` | 230 | UnwindData |  |
| 226 | `phoneDevSpecific` | `0x10080` | 244 | UnwindData |  |
| 227 | `phoneGetButtonInfo` | `0x102A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `phoneGetButtonInfoA` | `0x102B0` | 50 | UnwindData |  |
| 229 | `phoneGetButtonInfoW` | `0x102F0` | 119 | UnwindData |  |
| 230 | `phoneGetData` | `0x10370` | 121 | UnwindData |  |
| 231 | `phoneGetDevCaps` | `0x103F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `phoneGetDevCapsA` | `0x10400` | 124 | UnwindData |  |
| 233 | `phoneGetDevCapsW` | `0x10490` | 157 | UnwindData |  |
| 234 | `phoneGetDisplay` | `0x10540` | 115 | UnwindData |  |
| 235 | `phoneGetGain` | `0x105C0` | 119 | UnwindData |  |
| 236 | `phoneGetHookSwitch` | `0x10640` | 115 | UnwindData |  |
| 237 | `phoneGetID` | `0x106C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `phoneGetIDA` | `0x106D0` | 145 | UnwindData |  |
| 239 | `phoneGetIDW` | `0x10770` | 901 | UnwindData |  |
| 240 | `phoneGetIcon` | `0x10B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `phoneGetIconA` | `0x10B10` | 126 | UnwindData |  |
| 242 | `phoneGetIconW` | `0x10BA0` | 185 | UnwindData |  |
| 243 | `phoneGetLamp` | `0x10C60` | 119 | UnwindData |  |
| 244 | `phoneGetMessage` | `0x10CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `phoneGetRing` | `0x10D00` | 140 | UnwindData |  |
| 246 | `phoneGetStatus` | `0x10DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `phoneGetStatusA` | `0x10DB0` | 50 | UnwindData |  |
| 248 | `phoneGetStatusMessages` | `0x10DF0` | 153 | UnwindData |  |
| 249 | `phoneGetStatusW` | `0x10E90` | 115 | UnwindData |  |
| 250 | `phoneGetVolume` | `0x10F10` | 119 | UnwindData |  |
| 251 | `phoneInitialize` | `0x10F90` | 171 | UnwindData |  |
| 252 | `phoneInitializeExA` | `0x11050` | 178 | UnwindData |  |
| 253 | `phoneInitializeExW` | `0x11110` | 158 | UnwindData |  |
| 254 | `phoneNegotiateAPIVersion` | `0x111C0` | 184 | UnwindData |  |
| 255 | `phoneNegotiateExtVersion` | `0x11280` | 170 | UnwindData |  |
| 256 | `phoneOpen` | `0x11330` | 226 | UnwindData |  |
| 257 | `phoneSetButtonInfo` | `0x11420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `phoneSetButtonInfoA` | `0x11430` | 395 | UnwindData |  |
| 259 | `phoneSetButtonInfoW` | `0x115D0` | 119 | UnwindData |  |
| 260 | `phoneSetData` | `0x11650` | 121 | UnwindData |  |
| 261 | `phoneSetDisplay` | `0x116D0` | 136 | UnwindData |  |
| 262 | `phoneSetGain` | `0x11760` | 120 | UnwindData |  |
| 263 | `phoneSetHookSwitch` | `0x117E0` | 173 | UnwindData |  |
| 264 | `phoneSetLamp` | `0x118A0` | 120 | UnwindData |  |
| 265 | `phoneSetRing` | `0x11920` | 120 | UnwindData |  |
| 266 | `phoneSetStatusMessages` | `0x119A0` | 120 | UnwindData |  |
| 267 | `phoneSetVolume` | `0x11A20` | 120 | UnwindData |  |
| 268 | `phoneShutdown` | `0x11AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `tapiRequestDrop` | `0x11AB0` | 113 | UnwindData |  |
| 273 | `tapiRequestMakeCall` | `0x11B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `tapiRequestMakeCallA` | `0x11B40` | 378 | UnwindData |  |
| 275 | `tapiRequestMakeCallW` | `0x11CC0` | 875 | UnwindData |  |
| 276 | `tapiRequestMediaCall` | `0x12040` | 88 | UnwindData |  |
| 277 | `tapiRequestMediaCallA` | `0x120A0` | 645 | UnwindData |  |
| 278 | `tapiRequestMediaCallW` | `0x12330` | 370 | UnwindData |  |
| 5 | `MMCAddProvider` | `0x135A0` | 167 | UnwindData |  |
| 6 | `MMCConfigProvider` | `0x13650` | 181 | UnwindData |  |
| 7 | `MMCGetAvailableProviders` | `0x13710` | 244 | UnwindData |  |
| 8 | `MMCGetDeviceFlags` | `0x13810` | 275 | UnwindData |  |
| 9 | `MMCGetLineInfo` | `0x13930` | 244 | UnwindData |  |
| 10 | `MMCGetLineStatus` | `0x13A30` | 232 | UnwindData |  |
| 11 | `MMCGetPhoneInfo` | `0x13B20` | 244 | UnwindData |  |
| 12 | `MMCGetPhoneStatus` | `0x13C20` | 232 | UnwindData |  |
| 13 | `MMCGetProviderList` | `0x13D10` | 148 | UnwindData |  |
| 14 | `MMCGetServerConfig` | `0x13DB0` | 270 | UnwindData |  |
| 15 | `MMCInitialize` | `0x13ED0` | 1,155 | UnwindData |  |
| 16 | `MMCRemoveProvider` | `0x14360` | 181 | UnwindData |  |
| 17 | `MMCSetLineInfo` | `0x14420` | 244 | UnwindData |  |
| 18 | `MMCSetPhoneInfo` | `0x14520` | 244 | UnwindData |  |
| 19 | `MMCSetServerConfig` | `0x14620` | 297 | UnwindData |  |
| 20 | `MMCShutdown` | `0x14750` | 258 | UnwindData |  |
| 24 | `internalConfig` | `0x20A20` | 214 | UnwindData |  |
| 4 | `LocWizardDlgProc` | `0x23360` | 2,292 | UnwindData |  |
| 25 | `internalCreateDefLocation` | `0x25650` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `internalNewLocationW` | `0x256B0` | 686 | UnwindData |  |
| 28 | `internalRemoveLocation` | `0x25970` | 553 | UnwindData |  |
| 29 | `internalRenameLocationW` | `0x25BA0` | 486 | UnwindData |  |
| 133 | `lineGetTranslateCaps` | `0x25D90` | 105 | UnwindData |  |
| 134 | `lineGetTranslateCapsA` | `0x25E00` | 155 | UnwindData |  |
| 135 | `lineGetTranslateCapsW` | `0x25EB0` | 158 | UnwindData |  |
| 189 | `lineSetCurrentLocation` | `0x25F60` | 334 | UnwindData |  |
| 200 | `lineSetTollList` | `0x260C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `lineSetTollListA` | `0x260D0` | 216 | UnwindData |  |
| 202 | `lineSetTollListW` | `0x261B0` | 1,070 | UnwindData |  |
| 211 | `lineTranslateAddress` | `0x265F0` | 182 | UnwindData |  |
| 212 | `lineTranslateAddressA` | `0x266B0` | 290 | UnwindData |  |
| 213 | `lineTranslateAddressW` | `0x267E0` | 891 | UnwindData |  |
| 214 | `lineTranslateDialog` | `0x26B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `lineTranslateDialogA` | `0x26B80` | 257 | UnwindData |  |
| 216 | `lineTranslateDialogW` | `0x26C90` | 421 | UnwindData |  |
| 269 | `tapiGetLocationInfo` | `0x26E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `tapiGetLocationInfoA` | `0x26E50` | 335 | UnwindData |  |
| 271 | `tapiGetLocationInfoW` | `0x26FB0` | 301 | UnwindData |  |
