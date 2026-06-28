# Binary Specification: spoolss.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\spoolss.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `acf7574a3cd2991ad19c6db0ae529f8e8bec76e28b6bf3b0d1c41916bb853eaf`
* **Total Exported Functions:** 209

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 64 | `DllFreeSplMem` | `0x1B20` | 66 | UnwindData |  |
| 62 | `DllAllocSplMem` | `0x1B70` | 49 | UnwindData |  |
| 65 | `DllFreeSplStr` | `0x1BB0` | 73 | UnwindData |  |
| 176 | `SplIsUpgrade` | `0x1C00` | 85 | UnwindData |  |
| 35 | `CacheAddName` | `0x1C60` | 85 | UnwindData |  |
| 141 | `RevertToPrinterSelf` | `0x1CC0` | 49 | UnwindData |  |
| 31 | `AllocSplStr` | `0x1DE0` | 49 | UnwindData |  |
| 105 | `ImpersonatePrinterClient` | `0x1E20` | 49 | UnwindData |  |
| 123 | `PackStrings` | `0x1F60` | 78 | UnwindData |  |
| 43 | `CheckLocalCall` | `0x1FC0` | 85 | UnwindData |  |
| 40 | `CacheIsNameInNodeList` | `0x2020` | 85 | UnwindData |  |
| 121 | `OpenPrinterW` | `0x2080` | 93 | UnwindData |  |
| 100 | `GetPrinterDriverW` | `0x20F0` | 127 | UnwindData |  |
| 44 | `ClosePrinter` | `0x2180` | 93 | UnwindData |  |
| 107 | `IsNameTheLocalMachineOrAClusterSpooler` | `0x21F0` | 82 | UnwindData |  |
| 66 | `DllMain` | `0x2250` | 26 | UnwindData |  |
| 93 | `GetJobW` | `0x2300` | 126 | UnwindData |  |
| 164 | `SetPortW` | `0x2390` | 78 | UnwindData |  |
| 108 | `IsNamedPipeRpcCall` | `0x23F0` | 82 | UnwindData |  |
| 82 | `EnumPrintersW` | `0x2450` | 108 | UnwindData |  |
| 144 | `RouterAllocBidiResponseContainer` | `0x24D0` | 80 | UnwindData |  |
| 202 | `UpdatePrinterRegAllEx` | `0x2530` | 98 | UnwindData |  |
| 124 | `PartialReplyPrinterChangeNotification` | `0x25A0` | 80 | UnwindData |  |
| 101 | `GetPrinterW` | `0x2600` | 110 | UnwindData |  |
| 75 | `EnumPortsW` | `0x26B0` | 98 | UnwindData |  |
| 151 | `RouterFreeBidiResponseContainer` | `0x2720` | 83 | UnwindData |  |
| 102 | `GetServerPolicy` | `0x2780` | 83 | UnwindData |  |
| 97 | `GetPrinterDataW` | `0x27E0` | 119 | UnwindData |  |
| 109 | `MIDL_user_allocate1` | `0x2860` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `RouterAllocBidiMem` | `0x2860` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `OpenPrinterPort2W` | `0x2930` | 78 | UnwindData |  |
| 145 | `RouterAllocPrinterNotifyInfo` | `0x29A0` | 80 | UnwindData |  |
| 183 | `SplRegisterForSessionEvents` | `0x2A00` | 80 | UnwindData |  |
| 90 | `GetJobAttributes` | `0x2A60` | 72 | UnwindData |  |
| 91 | `GetJobAttributesEx` | `0x2AB0` | 941 | UnwindData |  |
| 137 | `ReplyPrinterChangeNotification` | `0x2E70` | 78 | UnwindData |  |
| 163 | `SetJobW` | `0x2ED0` | 101 | UnwindData |  |
| 130 | `ReadPrinter` | `0x2F70` | 88 | UnwindData |  |
| 205 | `WaitForSpoolerInitialization` | `0x2FD0` | 76 | UnwindData |  |
| 115 | `MarshallUpStructure` | `0x3030` | 88 | UnwindData |  |
| 167 | `SetPrinterW` | `0x30D0` | 75 | UnwindData |  |
| 80 | `EnumPrinterDriversW` | `0x3130` | 117 | UnwindData |  |
| 33 | `AppendPrinterNotifyInfoData` | `0x31B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `CallDrvDevModeConversion` | `0x31E0` | 120 | UnwindData |  |
| 32 | `AllowRemoteCalls` | `0x3260` | 83 | UnwindData |  |
| 166 | `SetPrinterDataW` | `0x32C0` | 90 | UnwindData |  |
| 96 | `GetPrinterDataExW` | `0x3320` | 160 | UnwindData |  |
| 206 | `WritePrinter` | `0x33D0` | 88 | UnwindData |  |
| 174 | `SplInitializeWinSpoolDrv` | `0x34B0` | 383 | UnwindData |  |
| 173 | `SplGetUserSidStringFromToken` | `0x3760` | 81 | UnwindData |  |
| 131 | `ReallocSplMem` | `0x37C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `RouterBroadcastMessage` | `0x37F0` | 91 | UnwindData |  |
| 88 | `FreePrintPropertyValue` | `0x3860` | 76 | UnwindData |  |
| 189 | `SpoolerFindFirstPrinterChangeNotification` | `0x38C0` | 145 | UnwindData |  |
| 110 | `MIDL_user_free1` | `0x3F10` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `RouterFreeBidiMem` | `0x3F10` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `DllAllocSplStr` | `0x4130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `DllReallocSplMem` | `0x4160` | 21,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `OpenPrinterExW` | `0x94D0` | 78 | UnwindData |  |
| 2 | `RouterCorePrinterDriverInstalled` | `0xA800` | 122 | UnwindData |  |
| 3 | `RouterCreatePrintAsyncNotificationChannel` | `0xA880` | 317 | UnwindData |  |
| 4 | `RouterDeletePrinterDriverPackage` | `0xA9D0` | 83 | UnwindData |  |
| 5 | `RouterGetCorePrinterDrivers` | `0xAA30` | 91 | UnwindData |  |
| 6 | `RouterGetPrintClassObject` | `0xAAA0` | 175 | UnwindData |  |
| 7 | `RouterGetPrinterDriverPackagePath` | `0xAB60` | 120 | UnwindData |  |
| 8 | `RouterInstallPrinterDriverFromPackage` | `0xABE0` | 91 | UnwindData |  |
| 9 | `RouterRegisterForPrintAsyncNotifications` | `0xAC50` | 101 | UnwindData |  |
| 10 | `RouterUnregisterForPrintAsyncNotifications` | `0xACC0` | 83 | UnwindData |  |
| 11 | `RouterUploadPrinterDriverPackage` | `0xAD20` | 101 | UnwindData |  |
| 12 | `AbortPrinter` | `0xCA60` | 80 | UnwindData |  |
| 13 | `AddFormW` | `0xCAC0` | 80 | UnwindData |  |
| 14 | `AddJobW` | `0xCB20` | 88 | UnwindData |  |
| 15 | `AddMonitorW` | `0xCB80` | 91 | UnwindData |  |
| 16 | `AddPerMachineConnectionW` | `0xCBF0` | 78 | UnwindData |  |
| 17 | `AddPortExW` | `0xCC50` | 78 | UnwindData |  |
| 18 | `AddPortW` | `0xCCB0` | 80 | UnwindData |  |
| 20 | `AddPrintProcessorW` | `0xCD10` | 78 | UnwindData |  |
| 21 | `AddPrintProvidorW` | `0xCD70` | 80 | UnwindData |  |
| 22 | `AddPrinterConnectionW` | `0xCDD0` | 77 | UnwindData |  |
| 23 | `AddPrinterDriverExW` | `0xCE30` | 78 | UnwindData |  |
| 24 | `AddPrinterDriverW` | `0xCE90` | 80 | UnwindData |  |
| 25 | `AddPrinterExW` | `0xCEF0` | 85 | UnwindData |  |
| 26 | `AddPrinterW` | `0xCF50` | 77 | UnwindData |  |
| 27 | `AdjustPointers` | `0xCFB0` | 78 | UnwindData |  |
| 28 | `AdjustPointersInStructuresArray` | `0xD010` | 88 | UnwindData |  |
| 29 | `AlignKMPtr` | `0xD070` | 114 | UnwindData |  |
| 30 | `AlignRpcPtr` | `0xD0F0` | 80 | UnwindData |  |
| 34 | `BuildOtherNamesFromMachineName` | `0xD150` | 80 | UnwindData |  |
| 36 | `CacheCreateAndAddNode` | `0xD1B0` | 83 | UnwindData |  |
| 37 | `CacheCreateAndAddNodeWithIPAddresses` | `0xD210` | 81 | UnwindData |  |
| 38 | `CacheDeleteNode` | `0xD270` | 83 | UnwindData |  |
| 39 | `CacheIsNameCluster` | `0xD2D0` | 83 | UnwindData |  |
| 42 | `CallRouterFindFirstPrinterChangeNotification` | `0xD330` | 91 | UnwindData |  |
| 45 | `ConfigurePortW` | `0xD3A0` | 80 | UnwindData |  |
| 46 | `CreatePrinterIC` | `0xD400` | 80 | UnwindData |  |
| 47 | `DeleteFormW` | `0xD460` | 80 | UnwindData |  |
| 48 | `DeleteJobNamedProperty` | `0xD4C0` | 83 | UnwindData |  |
| 49 | `DeleteMonitorW` | `0xD520` | 80 | UnwindData |  |
| 50 | `DeletePerMachineConnectionW` | `0xD580` | 80 | UnwindData |  |
| 51 | `DeletePortW` | `0xD5E0` | 91 | UnwindData |  |
| 52 | `DeletePrintProcessorW` | `0xD650` | 91 | UnwindData |  |
| 53 | `DeletePrintProvidorW` | `0xD6C0` | 80 | UnwindData |  |
| 54 | `DeletePrinter` | `0xD720` | 77 | UnwindData |  |
| 55 | `DeletePrinterConnectionW` | `0xD780` | 80 | UnwindData |  |
| 56 | `DeletePrinterDataExW` | `0xD7E0` | 83 | UnwindData |  |
| 57 | `DeletePrinterDataW` | `0xD840` | 83 | UnwindData |  |
| 58 | `DeletePrinterDriverExW` | `0xD8A0` | 88 | UnwindData |  |
| 59 | `DeletePrinterDriverW` | `0xD900` | 80 | UnwindData |  |
| 60 | `DeletePrinterIC` | `0xD960` | 80 | UnwindData |  |
| 61 | `DeletePrinterKeyW` | `0xD9C0` | 83 | UnwindData |  |
| 68 | `DllReallocSplStr` | `0xDA20` | 118 | UnwindData |  |
| 69 | `EndDocPrinter` | `0xDAA0` | 91 | UnwindData |  |
| 70 | `EndPagePrinter` | `0xDB10` | 91 | UnwindData |  |
| 71 | `EnumFormsW` | `0xDB80` | 135 | UnwindData |  |
| 72 | `EnumJobsW` | `0xDC10` | 192 | UnwindData |  |
| 73 | `EnumMonitorsW` | `0xDCE0` | 98 | UnwindData |  |
| 74 | `EnumPerMachineConnectionsW` | `0xDD50` | 88 | UnwindData |  |
| 76 | `EnumPrintProcessorDatatypesW` | `0xDDB0` | 117 | UnwindData |  |
| 77 | `EnumPrintProcessorsW` | `0xDE30` | 117 | UnwindData |  |
| 78 | `EnumPrinterDataExW` | `0xDEB0` | 101 | UnwindData |  |
| 79 | `EnumPrinterDataW` | `0xDF20` | 160 | UnwindData |  |
| 81 | `EnumPrinterKeyW` | `0xDFD0` | 91 | UnwindData |  |
| 83 | `FindClosePrinterChangeNotification` | `0xE040` | 80 | UnwindData |  |
| 84 | `FlushPrinter` | `0xE0A0` | 110 | UnwindData |  |
| 85 | `FormatPrinterForRegistryKey` | `0xE120` | 80 | UnwindData |  |
| 86 | `FormatRegistryKeyForPrinter` | `0xE180` | 80 | UnwindData |  |
| 87 | `FreeOtherNames` | `0xE1E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `GetFormW` | `0xE220` | 98 | UnwindData |  |
| 92 | `GetJobNamedPropertyValue` | `0xE290` | 81 | UnwindData |  |
| 94 | `GetNetworkId` | `0xE2F0` | 83 | UnwindData |  |
| 95 | `GetPrintProcessorDirectoryW` | `0xE350` | 131 | UnwindData |  |
| 98 | `GetPrinterDriverDirectoryW` | `0xE3E0` | 130 | UnwindData |  |
| 99 | `GetPrinterDriverExW` | `0xE470` | 179 | UnwindData |  |
| 103 | `GetShrinkedSize` | `0xE530` | 80 | UnwindData |  |
| 104 | `GetSpoolerTlsIndexes` | `0xE590` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `InitializeRouter` | `0xE5C0` | 58 | UnwindData |  |
| 113 | `MarshallDownStructure` | `0xE600` | 78 | UnwindData |  |
| 114 | `MarshallDownStructuresArray` | `0xE660` | 88 | UnwindData |  |
| 116 | `MarshallUpStructuresArray` | `0xE6C0` | 98 | UnwindData |  |
| 117 | `OldGetPrinterDriverW` | `0xE730` | 95 | UnwindData |  |
| 118 | `OpenPrinter2W` | `0xE7A0` | 78 | UnwindData |  |
| 120 | `OpenPrinterPortWithClientInfo` | `0xE800` | 98 | UnwindData |  |
| 125 | `PlayGdiScriptOnPrinterIC` | `0xE870` | 98 | UnwindData |  |
| 126 | `PrinterHandleRundown` | `0xE8E0` | 76 | UnwindData |  |
| 127 | `PrinterMessageBoxW` | `0xE940` | 101 | UnwindData |  |
| 128 | `ProvidorFindClosePrinterChangeNotification` | `0xE9B0` | 80 | UnwindData |  |
| 129 | `ProvidorFindFirstPrinterChangeNotification` | `0xEA10` | 98 | UnwindData |  |
| 132 | `ReallocSplStr` | `0xEA80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `RemoteFindFirstPrinterChangeNotification` | `0xEAB0` | 117 | UnwindData |  |
| 135 | `ReplyClosePrinter` | `0xEB30` | 80 | UnwindData |  |
| 136 | `ReplyOpenPrinter` | `0xEB90` | 88 | UnwindData |  |
| 138 | `ReplyPrinterChangeNotificationEx` | `0xEBF0` | 88 | UnwindData |  |
| 139 | `ReportJobProcessingProgress` | `0xEC50` | 81 | UnwindData |  |
| 140 | `ResetPrinterW` | `0xECB0` | 80 | UnwindData |  |
| 142 | `RouterAddPrinterConnection2` | `0xED10` | 80 | UnwindData |  |
| 147 | `RouterFindCompatibleDriver` | `0xED70` | 161 | UnwindData |  |
| 148 | `RouterFindFirstPrinterChangeNotification` | `0xEE20` | 98 | UnwindData |  |
| 149 | `RouterFindNextPrinterChangeNotification` | `0xEE90` | 88 | UnwindData |  |
| 152 | `RouterFreePrinterNotifyInfo` | `0xEEF0` | 80 | UnwindData |  |
| 153 | `RouterInstallPrinterDriverPackageFromConnection` | `0xEF50` | 83 | UnwindData |  |
| 154 | `RouterInternalGetPrinterDriver` | `0xEFB0` | 182 | UnwindData |  |
| 155 | `RouterRefreshPrinterChangeNotification` | `0xF070` | 78 | UnwindData |  |
| 156 | `RouterReplyPrinter` | `0xF0D0` | 98 | UnwindData |  |
| 157 | `RouterSpoolerSetPolicy` | `0xF140` | 83 | UnwindData |  |
| 158 | `ScheduleJob` | `0xF1A0` | 80 | UnwindData |  |
| 159 | `SeekPrinter` | `0xF200` | 88 | UnwindData |  |
| 160 | `SendRecvBidiData` | `0xF260` | 81 | UnwindData |  |
| 161 | `SetFormW` | `0xF2C0` | 78 | UnwindData |  |
| 162 | `SetJobNamedProperty` | `0xF320` | 83 | UnwindData |  |
| 165 | `SetPrinterDataExW` | `0xF380` | 119 | UnwindData |  |
| 168 | `SplCloseSpoolFileHandle` | `0xF400` | 80 | UnwindData |  |
| 169 | `SplCommitSpoolData` | `0xF460` | 117 | UnwindData |  |
| 170 | `SplDriverUnloadComplete` | `0xF4E0` | 76 | UnwindData |  |
| 171 | `SplGetClientUserHandle` | `0xF540` | 80 | UnwindData |  |
| 172 | `SplGetSpoolFileInfo` | `0xF5A0` | 98 | UnwindData |  |
| 175 | `SplIsSessionZero` | `0xF610` | 83 | UnwindData |  |
| 177 | `SplProcessPnPEvent` | `0xF670` | 80 | UnwindData |  |
| 178 | `SplProcessSessionEvent` | `0xF6D0` | 83 | UnwindData |  |
| 179 | `SplPromptUIInUsersSession` | `0xF730` | 78 | UnwindData |  |
| 180 | `SplQueryUserInfo` | `0xF790` | 83 | UnwindData |  |
| 181 | `SplReadPrinter` | `0xF7F0` | 80 | UnwindData |  |
| 182 | `SplRegisterForDeviceEvents` | `0xF850` | 80 | UnwindData |  |
| 184 | `SplShutDownRouter` | `0xF8B0` | 76 | UnwindData |  |
| 185 | `SplUalCollectData` | `0xF910` | 83 | UnwindData |  |
| 186 | `SplUnregisterForDeviceEvents` | `0xF970` | 80 | UnwindData |  |
| 187 | `SplUnregisterForSessionEvents` | `0xF9D0` | 80 | UnwindData |  |
| 188 | `SpoolerFindClosePrinterChangeNotification` | `0xFA30` | 80 | UnwindData |  |
| 190 | `SpoolerFindNextPrinterChangeNotification` | `0xFA90` | 78 | UnwindData |  |
| 191 | `SpoolerFreePrinterNotifyInfo` | `0xFAF0` | 76 | UnwindData |  |
| 192 | `SpoolerHasInitialized` | `0xFB50` | 80 | UnwindData |  |
| 193 | `SpoolerInit` | `0xFBB0` | 80 | UnwindData |  |
| 194 | `SpoolerRefreshPrinterChangeNotification` | `0xFC10` | 78 | UnwindData |  |
| 195 | `StartDocPrinterW` | `0xFC70` | 91 | UnwindData |  |
| 196 | `StartPagePrinter` | `0xFCE0` | 91 | UnwindData |  |
| 197 | `UndoAlignKMPtr` | `0xFD50` | 52 | UnwindData |  |
| 198 | `UndoAlignRpcPtr` | `0xFD90` | 101 | UnwindData |  |
| 199 | `UpdateBufferSize` | `0xFE00` | 101 | UnwindData |  |
| 201 | `UpdatePrinterRegAll` | `0xFE70` | 78 | UnwindData |  |
| 203 | `UpdatePrinterRegUser` | `0xFED0` | 91 | UnwindData |  |
| 204 | `WaitForPrinterChange` | `0xFF40` | 80 | UnwindData |  |
| 207 | `XcvDataW` | `0xFFA0` | 145 | UnwindData |  |
| 208 | `bGetDevModePerUser` | `0x10040` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `bSetDevModePerUser` | `0x10070` | 9,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `MakeOffset` | `0x124A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `MakePTR` | `0x124B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `PackStringToEOB` | `0x124C0` | 75 | UnwindData |  |
| 19 | `AddPrintDeviceObject` | `0x13C30` | 181 | UnwindData |  |
| 134 | `RemovePrintDeviceObject` | `0x13CF0` | 66 | UnwindData |  |
| 200 | `UpdatePrintDeviceObject` | `0x13D40` | 340 | UnwindData |  |
