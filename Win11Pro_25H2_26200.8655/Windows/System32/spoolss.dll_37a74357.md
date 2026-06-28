# Binary Specification: spoolss.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\spoolss.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `37a74357145754c16e0c7a73eadb2c568e9e0115a9984f6ed19b225dfdb24d6c`
* **Total Exported Functions:** 209

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 64 | `DllFreeSplMem` | `0x1B30` | 66 | UnwindData |  |
| 62 | `DllAllocSplMem` | `0x1B80` | 49 | UnwindData |  |
| 65 | `DllFreeSplStr` | `0x1BC0` | 73 | UnwindData |  |
| 176 | `SplIsUpgrade` | `0x1C10` | 85 | UnwindData |  |
| 35 | `CacheAddName` | `0x1C70` | 85 | UnwindData |  |
| 141 | `RevertToPrinterSelf` | `0x1CD0` | 49 | UnwindData |  |
| 31 | `AllocSplStr` | `0x1DF0` | 49 | UnwindData |  |
| 105 | `ImpersonatePrinterClient` | `0x1E30` | 49 | UnwindData |  |
| 123 | `PackStrings` | `0x1F70` | 78 | UnwindData |  |
| 43 | `CheckLocalCall` | `0x1FD0` | 85 | UnwindData |  |
| 40 | `CacheIsNameInNodeList` | `0x2030` | 85 | UnwindData |  |
| 121 | `OpenPrinterW` | `0x2090` | 93 | UnwindData |  |
| 100 | `GetPrinterDriverW` | `0x2100` | 127 | UnwindData |  |
| 44 | `ClosePrinter` | `0x2190` | 93 | UnwindData |  |
| 107 | `IsNameTheLocalMachineOrAClusterSpooler` | `0x2200` | 82 | UnwindData |  |
| 66 | `DllMain` | `0x2260` | 26 | UnwindData |  |
| 93 | `GetJobW` | `0x2310` | 126 | UnwindData |  |
| 164 | `SetPortW` | `0x23A0` | 78 | UnwindData |  |
| 108 | `IsNamedPipeRpcCall` | `0x2400` | 82 | UnwindData |  |
| 82 | `EnumPrintersW` | `0x2460` | 108 | UnwindData |  |
| 144 | `RouterAllocBidiResponseContainer` | `0x24E0` | 80 | UnwindData |  |
| 202 | `UpdatePrinterRegAllEx` | `0x2540` | 98 | UnwindData |  |
| 124 | `PartialReplyPrinterChangeNotification` | `0x25B0` | 80 | UnwindData |  |
| 101 | `GetPrinterW` | `0x2610` | 110 | UnwindData |  |
| 75 | `EnumPortsW` | `0x26C0` | 98 | UnwindData |  |
| 151 | `RouterFreeBidiResponseContainer` | `0x2730` | 83 | UnwindData |  |
| 102 | `GetServerPolicy` | `0x2790` | 83 | UnwindData |  |
| 97 | `GetPrinterDataW` | `0x27F0` | 119 | UnwindData |  |
| 109 | `MIDL_user_allocate1` | `0x2870` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `RouterAllocBidiMem` | `0x2870` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `OpenPrinterPort2W` | `0x2940` | 78 | UnwindData |  |
| 145 | `RouterAllocPrinterNotifyInfo` | `0x29B0` | 80 | UnwindData |  |
| 183 | `SplRegisterForSessionEvents` | `0x2A10` | 80 | UnwindData |  |
| 90 | `GetJobAttributes` | `0x2A70` | 72 | UnwindData |  |
| 91 | `GetJobAttributesEx` | `0x2AC0` | 941 | UnwindData |  |
| 137 | `ReplyPrinterChangeNotification` | `0x2E80` | 78 | UnwindData |  |
| 163 | `SetJobW` | `0x2EE0` | 101 | UnwindData |  |
| 130 | `ReadPrinter` | `0x2F80` | 88 | UnwindData |  |
| 205 | `WaitForSpoolerInitialization` | `0x2FE0` | 76 | UnwindData |  |
| 115 | `MarshallUpStructure` | `0x3040` | 88 | UnwindData |  |
| 167 | `SetPrinterW` | `0x30E0` | 75 | UnwindData |  |
| 80 | `EnumPrinterDriversW` | `0x3140` | 117 | UnwindData |  |
| 33 | `AppendPrinterNotifyInfoData` | `0x31C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `CallDrvDevModeConversion` | `0x31F0` | 120 | UnwindData |  |
| 32 | `AllowRemoteCalls` | `0x3270` | 83 | UnwindData |  |
| 166 | `SetPrinterDataW` | `0x32D0` | 90 | UnwindData |  |
| 96 | `GetPrinterDataExW` | `0x3330` | 160 | UnwindData |  |
| 206 | `WritePrinter` | `0x33E0` | 88 | UnwindData |  |
| 174 | `SplInitializeWinSpoolDrv` | `0x34C0` | 383 | UnwindData |  |
| 173 | `SplGetUserSidStringFromToken` | `0x36F0` | 81 | UnwindData |  |
| 131 | `ReallocSplMem` | `0x3750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `RouterBroadcastMessage` | `0x3780` | 91 | UnwindData |  |
| 88 | `FreePrintPropertyValue` | `0x37F0` | 76 | UnwindData |  |
| 189 | `SpoolerFindFirstPrinterChangeNotification` | `0x3850` | 145 | UnwindData |  |
| 110 | `MIDL_user_free1` | `0x3EA0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `RouterFreeBidiMem` | `0x3EA0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `DllAllocSplStr` | `0x40C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `DllReallocSplMem` | `0x40F0` | 20,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `OpenPrinterExW` | `0x91C0` | 78 | UnwindData |  |
| 2 | `RouterCorePrinterDriverInstalled` | `0xA570` | 122 | UnwindData |  |
| 3 | `RouterCreatePrintAsyncNotificationChannel` | `0xA5F0` | 317 | UnwindData |  |
| 4 | `RouterDeletePrinterDriverPackage` | `0xA740` | 83 | UnwindData |  |
| 5 | `RouterGetCorePrinterDrivers` | `0xA7A0` | 91 | UnwindData |  |
| 6 | `RouterGetPrintClassObject` | `0xA810` | 175 | UnwindData |  |
| 7 | `RouterGetPrinterDriverPackagePath` | `0xA8D0` | 120 | UnwindData |  |
| 8 | `RouterInstallPrinterDriverFromPackage` | `0xA950` | 91 | UnwindData |  |
| 9 | `RouterRegisterForPrintAsyncNotifications` | `0xA9C0` | 101 | UnwindData |  |
| 10 | `RouterUnregisterForPrintAsyncNotifications` | `0xAA30` | 83 | UnwindData |  |
| 11 | `RouterUploadPrinterDriverPackage` | `0xAA90` | 101 | UnwindData |  |
| 12 | `AbortPrinter` | `0xC810` | 80 | UnwindData |  |
| 13 | `AddFormW` | `0xC870` | 80 | UnwindData |  |
| 14 | `AddJobW` | `0xC8D0` | 88 | UnwindData |  |
| 15 | `AddMonitorW` | `0xC930` | 91 | UnwindData |  |
| 16 | `AddPerMachineConnectionW` | `0xC9A0` | 78 | UnwindData |  |
| 17 | `AddPortExW` | `0xCA00` | 78 | UnwindData |  |
| 18 | `AddPortW` | `0xCA60` | 80 | UnwindData |  |
| 20 | `AddPrintProcessorW` | `0xCAC0` | 78 | UnwindData |  |
| 21 | `AddPrintProvidorW` | `0xCB20` | 80 | UnwindData |  |
| 22 | `AddPrinterConnectionW` | `0xCB80` | 77 | UnwindData |  |
| 23 | `AddPrinterDriverExW` | `0xCBE0` | 78 | UnwindData |  |
| 24 | `AddPrinterDriverW` | `0xCC40` | 80 | UnwindData |  |
| 25 | `AddPrinterExW` | `0xCCA0` | 85 | UnwindData |  |
| 26 | `AddPrinterW` | `0xCD00` | 77 | UnwindData |  |
| 27 | `AdjustPointers` | `0xCD60` | 78 | UnwindData |  |
| 28 | `AdjustPointersInStructuresArray` | `0xCDC0` | 88 | UnwindData |  |
| 29 | `AlignKMPtr` | `0xCE20` | 114 | UnwindData |  |
| 30 | `AlignRpcPtr` | `0xCEA0` | 80 | UnwindData |  |
| 34 | `BuildOtherNamesFromMachineName` | `0xCF00` | 80 | UnwindData |  |
| 36 | `CacheCreateAndAddNode` | `0xCF60` | 83 | UnwindData |  |
| 37 | `CacheCreateAndAddNodeWithIPAddresses` | `0xCFC0` | 81 | UnwindData |  |
| 38 | `CacheDeleteNode` | `0xD020` | 83 | UnwindData |  |
| 39 | `CacheIsNameCluster` | `0xD080` | 83 | UnwindData |  |
| 42 | `CallRouterFindFirstPrinterChangeNotification` | `0xD0E0` | 91 | UnwindData |  |
| 45 | `ConfigurePortW` | `0xD150` | 80 | UnwindData |  |
| 46 | `CreatePrinterIC` | `0xD1B0` | 80 | UnwindData |  |
| 47 | `DeleteFormW` | `0xD210` | 80 | UnwindData |  |
| 48 | `DeleteJobNamedProperty` | `0xD270` | 83 | UnwindData |  |
| 49 | `DeleteMonitorW` | `0xD2D0` | 80 | UnwindData |  |
| 50 | `DeletePerMachineConnectionW` | `0xD330` | 80 | UnwindData |  |
| 51 | `DeletePortW` | `0xD390` | 91 | UnwindData |  |
| 52 | `DeletePrintProcessorW` | `0xD400` | 91 | UnwindData |  |
| 53 | `DeletePrintProvidorW` | `0xD470` | 80 | UnwindData |  |
| 54 | `DeletePrinter` | `0xD4D0` | 77 | UnwindData |  |
| 55 | `DeletePrinterConnectionW` | `0xD530` | 80 | UnwindData |  |
| 56 | `DeletePrinterDataExW` | `0xD590` | 83 | UnwindData |  |
| 57 | `DeletePrinterDataW` | `0xD5F0` | 83 | UnwindData |  |
| 58 | `DeletePrinterDriverExW` | `0xD650` | 88 | UnwindData |  |
| 59 | `DeletePrinterDriverW` | `0xD6B0` | 80 | UnwindData |  |
| 60 | `DeletePrinterIC` | `0xD710` | 80 | UnwindData |  |
| 61 | `DeletePrinterKeyW` | `0xD770` | 83 | UnwindData |  |
| 68 | `DllReallocSplStr` | `0xD7D0` | 118 | UnwindData |  |
| 69 | `EndDocPrinter` | `0xD850` | 91 | UnwindData |  |
| 70 | `EndPagePrinter` | `0xD8C0` | 91 | UnwindData |  |
| 71 | `EnumFormsW` | `0xD930` | 135 | UnwindData |  |
| 72 | `EnumJobsW` | `0xD9C0` | 192 | UnwindData |  |
| 73 | `EnumMonitorsW` | `0xDA90` | 98 | UnwindData |  |
| 74 | `EnumPerMachineConnectionsW` | `0xDB00` | 88 | UnwindData |  |
| 76 | `EnumPrintProcessorDatatypesW` | `0xDB60` | 117 | UnwindData |  |
| 77 | `EnumPrintProcessorsW` | `0xDBE0` | 117 | UnwindData |  |
| 78 | `EnumPrinterDataExW` | `0xDC60` | 101 | UnwindData |  |
| 79 | `EnumPrinterDataW` | `0xDCD0` | 160 | UnwindData |  |
| 81 | `EnumPrinterKeyW` | `0xDD80` | 91 | UnwindData |  |
| 83 | `FindClosePrinterChangeNotification` | `0xDDF0` | 80 | UnwindData |  |
| 84 | `FlushPrinter` | `0xDE50` | 110 | UnwindData |  |
| 85 | `FormatPrinterForRegistryKey` | `0xDED0` | 80 | UnwindData |  |
| 86 | `FormatRegistryKeyForPrinter` | `0xDF30` | 80 | UnwindData |  |
| 87 | `FreeOtherNames` | `0xDF90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `GetFormW` | `0xDFD0` | 98 | UnwindData |  |
| 92 | `GetJobNamedPropertyValue` | `0xE040` | 81 | UnwindData |  |
| 94 | `GetNetworkId` | `0xE0A0` | 83 | UnwindData |  |
| 95 | `GetPrintProcessorDirectoryW` | `0xE100` | 131 | UnwindData |  |
| 98 | `GetPrinterDriverDirectoryW` | `0xE190` | 130 | UnwindData |  |
| 99 | `GetPrinterDriverExW` | `0xE220` | 179 | UnwindData |  |
| 103 | `GetShrinkedSize` | `0xE2E0` | 80 | UnwindData |  |
| 104 | `GetSpoolerTlsIndexes` | `0xE340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `InitializeRouter` | `0xE370` | 58 | UnwindData |  |
| 113 | `MarshallDownStructure` | `0xE3B0` | 78 | UnwindData |  |
| 114 | `MarshallDownStructuresArray` | `0xE410` | 88 | UnwindData |  |
| 116 | `MarshallUpStructuresArray` | `0xE470` | 98 | UnwindData |  |
| 117 | `OldGetPrinterDriverW` | `0xE4E0` | 95 | UnwindData |  |
| 118 | `OpenPrinter2W` | `0xE550` | 78 | UnwindData |  |
| 120 | `OpenPrinterPortWithClientInfo` | `0xE5B0` | 98 | UnwindData |  |
| 125 | `PlayGdiScriptOnPrinterIC` | `0xE620` | 98 | UnwindData |  |
| 126 | `PrinterHandleRundown` | `0xE690` | 76 | UnwindData |  |
| 127 | `PrinterMessageBoxW` | `0xE6F0` | 101 | UnwindData |  |
| 128 | `ProvidorFindClosePrinterChangeNotification` | `0xE760` | 80 | UnwindData |  |
| 129 | `ProvidorFindFirstPrinterChangeNotification` | `0xE7C0` | 98 | UnwindData |  |
| 132 | `ReallocSplStr` | `0xE830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `RemoteFindFirstPrinterChangeNotification` | `0xE860` | 117 | UnwindData |  |
| 135 | `ReplyClosePrinter` | `0xE8E0` | 80 | UnwindData |  |
| 136 | `ReplyOpenPrinter` | `0xE940` | 88 | UnwindData |  |
| 138 | `ReplyPrinterChangeNotificationEx` | `0xE9A0` | 88 | UnwindData |  |
| 139 | `ReportJobProcessingProgress` | `0xEA00` | 81 | UnwindData |  |
| 140 | `ResetPrinterW` | `0xEA60` | 80 | UnwindData |  |
| 142 | `RouterAddPrinterConnection2` | `0xEAC0` | 80 | UnwindData |  |
| 147 | `RouterFindCompatibleDriver` | `0xEB20` | 161 | UnwindData |  |
| 148 | `RouterFindFirstPrinterChangeNotification` | `0xEBD0` | 98 | UnwindData |  |
| 149 | `RouterFindNextPrinterChangeNotification` | `0xEC40` | 88 | UnwindData |  |
| 152 | `RouterFreePrinterNotifyInfo` | `0xECA0` | 80 | UnwindData |  |
| 153 | `RouterInstallPrinterDriverPackageFromConnection` | `0xED00` | 83 | UnwindData |  |
| 154 | `RouterInternalGetPrinterDriver` | `0xED60` | 182 | UnwindData |  |
| 155 | `RouterRefreshPrinterChangeNotification` | `0xEE20` | 78 | UnwindData |  |
| 156 | `RouterReplyPrinter` | `0xEE80` | 98 | UnwindData |  |
| 157 | `RouterSpoolerSetPolicy` | `0xEEF0` | 83 | UnwindData |  |
| 158 | `ScheduleJob` | `0xEF50` | 80 | UnwindData |  |
| 159 | `SeekPrinter` | `0xEFB0` | 88 | UnwindData |  |
| 160 | `SendRecvBidiData` | `0xF010` | 81 | UnwindData |  |
| 161 | `SetFormW` | `0xF070` | 78 | UnwindData |  |
| 162 | `SetJobNamedProperty` | `0xF0D0` | 83 | UnwindData |  |
| 165 | `SetPrinterDataExW` | `0xF130` | 119 | UnwindData |  |
| 168 | `SplCloseSpoolFileHandle` | `0xF1B0` | 80 | UnwindData |  |
| 169 | `SplCommitSpoolData` | `0xF210` | 117 | UnwindData |  |
| 170 | `SplDriverUnloadComplete` | `0xF290` | 76 | UnwindData |  |
| 171 | `SplGetClientUserHandle` | `0xF2F0` | 80 | UnwindData |  |
| 172 | `SplGetSpoolFileInfo` | `0xF350` | 98 | UnwindData |  |
| 175 | `SplIsSessionZero` | `0xF3C0` | 83 | UnwindData |  |
| 177 | `SplProcessPnPEvent` | `0xF420` | 80 | UnwindData |  |
| 178 | `SplProcessSessionEvent` | `0xF480` | 83 | UnwindData |  |
| 179 | `SplPromptUIInUsersSession` | `0xF4E0` | 78 | UnwindData |  |
| 180 | `SplQueryUserInfo` | `0xF540` | 83 | UnwindData |  |
| 181 | `SplReadPrinter` | `0xF5A0` | 80 | UnwindData |  |
| 182 | `SplRegisterForDeviceEvents` | `0xF600` | 80 | UnwindData |  |
| 184 | `SplShutDownRouter` | `0xF660` | 76 | UnwindData |  |
| 185 | `SplUalCollectData` | `0xF6C0` | 83 | UnwindData |  |
| 186 | `SplUnregisterForDeviceEvents` | `0xF720` | 80 | UnwindData |  |
| 187 | `SplUnregisterForSessionEvents` | `0xF780` | 80 | UnwindData |  |
| 188 | `SpoolerFindClosePrinterChangeNotification` | `0xF7E0` | 80 | UnwindData |  |
| 190 | `SpoolerFindNextPrinterChangeNotification` | `0xF840` | 78 | UnwindData |  |
| 191 | `SpoolerFreePrinterNotifyInfo` | `0xF8A0` | 76 | UnwindData |  |
| 192 | `SpoolerHasInitialized` | `0xF900` | 80 | UnwindData |  |
| 193 | `SpoolerInit` | `0xF960` | 80 | UnwindData |  |
| 194 | `SpoolerRefreshPrinterChangeNotification` | `0xF9C0` | 78 | UnwindData |  |
| 195 | `StartDocPrinterW` | `0xFA20` | 91 | UnwindData |  |
| 196 | `StartPagePrinter` | `0xFA90` | 91 | UnwindData |  |
| 197 | `UndoAlignKMPtr` | `0xFB00` | 52 | UnwindData |  |
| 198 | `UndoAlignRpcPtr` | `0xFB40` | 101 | UnwindData |  |
| 199 | `UpdateBufferSize` | `0xFBB0` | 101 | UnwindData |  |
| 201 | `UpdatePrinterRegAll` | `0xFC20` | 78 | UnwindData |  |
| 203 | `UpdatePrinterRegUser` | `0xFC80` | 91 | UnwindData |  |
| 204 | `WaitForPrinterChange` | `0xFCF0` | 80 | UnwindData |  |
| 207 | `XcvDataW` | `0xFD50` | 145 | UnwindData |  |
| 208 | `bGetDevModePerUser` | `0xFDF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `bSetDevModePerUser` | `0xFE20` | 9,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `MakeOffset` | `0x12250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `MakePTR` | `0x12260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `PackStringToEOB` | `0x12270` | 75 | UnwindData |  |
| 19 | `AddPrintDeviceObject` | `0x139E0` | 181 | UnwindData |  |
| 134 | `RemovePrintDeviceObject` | `0x13AA0` | 66 | UnwindData |  |
| 200 | `UpdatePrintDeviceObject` | `0x13AF0` | 340 | UnwindData |  |
