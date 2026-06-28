# Binary Specification: msoert2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msoert2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8204500996a06940aaca0b5fcf49bbcd532efb6676f1209109d01b281afac9fd`
* **Total Exported Functions:** 208

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 93 | `FIsEmptyW` | `0x1070` | 103 | UnwindData |  |
| 180 | `PszToUnicode` | `0x1180` | 26 | UnwindData |  |
| 97 | `FIsSpaceW` | `0x1280` | 64 | UnwindData |  |
| 175 | `PszScanToCharA` | `0x1620` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `PszToANSI` | `0x1650` | 28 | UnwindData |  |
| 129 | `HrIndexOfWeek` | `0x1770` | 138 | UnwindData |  |
| 142 | `IsDigit` | `0x1840` | 94 | UnwindData |  |
| 71 | `ChConvertFromHex` | `0x18B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `OpenFileStreamShareW` | `0x18E0` | 34 | UnwindData |  |
| 166 | `PszAllocA` | `0x19A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `PszDupA` | `0x19D0` | 20 | UnwindData |  |
| 14 | `FInitializeRichEdit` | `0x1BA0` | 152 | UnwindData |  |
| 128 | `HrIndexOfMonth` | `0x1C90` | 161 | UnwindData |  |
| 75 | `CopyRegistry` | `0x2D80` | 478 | UnwindData |  |
| 100 | `FMissingCert` | `0x2F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `HrBSTRToLPSZ` | `0x2F90` | 36 | UnwindData |  |
| 126 | `HrIStreamToBSTR` | `0x2FC0` | 259 | UnwindData |  |
| 127 | `HrIStreamWToBSTR` | `0x30D0` | 294 | UnwindData |  |
| 131 | `HrLPSZCPToBSTR` | `0x3200` | 334 | UnwindData |  |
| 132 | `HrLPSZToBSTR` | `0x3360` | 51 | UnwindData |  |
| 9 | `CryptAllocFunc` | `0x33A0` | 38 | UnwindData |  |
| 13 | `CryptFreeFunc` | `0x33D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `HrGetCertKeyUsage` | `0x33F0` | 202 | UnwindData |  |
| 115 | `HrDecodeObject` | `0x3660` | 137 | UnwindData |  |
| 120 | `HrGetCertificateParam` | `0x36F0` | 216 | UnwindData |  |
| 122 | `HrGetMsgParam` | `0x37D0` | 252 | UnwindData |  |
| 163 | `PVDecodeObject` | `0x38E0` | 64 | UnwindData |  |
| 164 | `PVGetCertificateParam` | `0x3930` | 47 | UnwindData |  |
| 165 | `PVGetMsgParam` | `0x3970` | 63 | UnwindData |  |
| 160 | *Ordinal Only* | `0x3B20` | 61 | UnwindData |  |
| 191 | `SzGetCertificateEmailAddress` | `0x3B70` | 157 | UnwindData |  |
| 2 | `CreateSystemHandleName` | `0x3CA0` | 216 | UnwindData |  |
| 79 | `CreateLogFile` | `0x4B90` | 209 | UnwindData |  |
| 77 | `CreateDataObject` | `0x4F90` | 172 | UnwindData |  |
| 48 | `CchFileTimeToDateTimeSz` | `0x5810` | 383 | UnwindData |  |
| 51 | `CchFileTimeToDateTimeW` | `0x59A0` | 398 | UnwindData |  |
| 15 | `GetDllMajorVersion` | `0x5B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `DllCanUnloadNow` | `0x5B50` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `CreateEnumFormatEtc` | `0x6050` | 237 | UnwindData |  |
| 89 | `DllGetClassObject` | `0x6150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | *Ordinal Only* | `0x6180` | 127 | UnwindData |  |
| 19 | `GetHtmlCharset` | `0x63B0` | 229 | UnwindData |  |
| 17 | *Ordinal Only* | `0x6850` | 301 | UnwindData |  |
| 11 | *Ordinal Only* | `0x6990` | 40 | UnwindData |  |
| 12 | *Ordinal Only* | `0x69C0` | 70 | UnwindData |  |
| 10 | *Ordinal Only* | `0x6A10` | 60 | UnwindData |  |
| 16 | *Ordinal Only* | `0x6A60` | 557 | UnwindData |  |
| 46 | *Ordinal Only* | `0x6CA0` | 880 | UnwindData |  |
| 39 | *Ordinal Only* | `0x83D0` | 142 | UnwindData |  |
| 107 | `HrCheckTridentMenu` | `0x8470` | 459 | UnwindData |  |
| 114 | `HrCreateTridentMenu` | `0x8650` | 474 | UnwindData |  |
| 119 | `HrGetBodyElement` | `0x8830` | 126 | UnwindData |  |
| 121 | `HrGetElementImpl` | `0x88C0` | 298 | UnwindData |  |
| 125 | `HrGetStyleSheet` | `0x89F0` | 324 | UnwindData |  |
| 135 | `HrSetDirtyFlagImpl` | `0x8B40` | 184 | UnwindData |  |
| 76 | `CrackNotificationPackage` | `0x9660` | 261 | UnwindData |  |
| 80 | `CreateNotify` | `0x9770` | 89 | UnwindData |  |
| 23 | `GetStoreRootDirectoryFromRegistryEntry` | `0xA060` | 189 | UnwindData |  |
| 28 | `GetStoreRootDirectoryFromRegistryEntryW` | `0xA130` | 205 | UnwindData |  |
| 200 | *Ordinal Only* | `0xA210` | 163 | UnwindData |  |
| 3 | *Ordinal Only* | `0xA2C0` | 61 | UnwindData |  |
| 70 | *Ordinal Only* | `0xA310` | 61 | UnwindData |  |
| 59 | *Ordinal Only* | `0xA360` | 52 | UnwindData |  |
| 32 | `IsHttpUrlA` | `0xA3A0` | 93 | UnwindData |  |
| 33 | `IsHttpUrlW` | `0xA410` | 93 | UnwindData |  |
| 36 | `AppendTempFileList` | `0xAB60` | 347 | UnwindData |  |
| 37 | `BrowseForFolder` | `0xACD0` | 171 | UnwindData |  |
| 47 | `BrowseForFolderW` | `0xAD90` | 263 | UnwindData |  |
| 66 | `CenterDialog` | `0xAEA0` | 387 | UnwindData |  |
| 74 | `CleanupGlobalTempFiles` | `0xB030` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `CreateTempFile` | `0xB160` | 462 | UnwindData |  |
| 85 | `CreateTempFileW` | `0xB340` | 652 | UnwindData |  |
| 86 | `DeleteTempFile` | `0xB5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `DeleteTempFileOnShutdownEx` | `0xB5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `FBuildTempPath` | `0xB610` | 231 | UnwindData |  |
| 91 | `FBuildTempPathW` | `0xB700` | 767 | UnwindData |  |
| 94 | `FIsHTMLFile` | `0xBA10` | 203 | UnwindData |  |
| 95 | `FIsHTMLFileW` | `0xBAF0` | 205 | UnwindData |  |
| 101 | `FreeTempFileList` | `0xBBD0` | 65 | UnwindData |  |
| 102 | `GenerateUniqueFileName` | `0xBC20` | 665 | UnwindData |  |
| 103 | `GenerateUniqueFileNameW` | `0xBEC0` | 416 | UnwindData |  |
| 104 | `GetExePath` | `0xC070` | 364 | UnwindData |  |
| 105 | `GetTopMostParent` | `0xC1F0` | 100 | UnwindData |  |
| 159 | *Ordinal Only* | `0xC260` | 702 | UnwindData |  |
| 1 | *Ordinal Only* | `0xC530` | 176 | UnwindData |  |
| 61 | *Ordinal Only* | `0xC5F0` | 126 | UnwindData |  |
| 54 | *Ordinal Only* | `0xC680` | 34 | UnwindData |  |
| 55 | *Ordinal Only* | `0xC6B0` | 79 | UnwindData |  |
| 62 | *Ordinal Only* | `0xC710` | 96 | UnwindData |  |
| 60 | *Ordinal Only* | `0xC780` | 66 | UnwindData |  |
| 50 | *Ordinal Only* | `0xC7D0` | 44 | UnwindData |  |
| 56 | *Ordinal Only* | `0xC810` | 133 | UnwindData |  |
| 52 | *Ordinal Only* | `0xC8A0` | 54 | UnwindData |  |
| 63 | *Ordinal Only* | `0xC8E0` | 59 | UnwindData |  |
| 64 | *Ordinal Only* | `0xC930` | 59 | UnwindData |  |
| 53 | *Ordinal Only* | `0xC980` | 52 | UnwindData |  |
| 8 | *Ordinal Only* | `0xC9C0` | 53 | UnwindData |  |
| 57 | *Ordinal Only* | `0xCA00` | 54 | UnwindData |  |
| 7 | *Ordinal Only* | `0xCA40` | 67 | UnwindData |  |
| 58 | *Ordinal Only* | `0xCA90` | 52 | UnwindData |  |
| 141 | `IDrawText` | `0xCAD0` | 401 | UnwindData |  |
| 4 | *Ordinal Only* | `0xCC70` | 432 | UnwindData |  |
| 67 | *Ordinal Only* | `0xCE30` | 450 | UnwindData |  |
| 146 | `MessageBoxInst` | `0xD000` | 551 | UnwindData |  |
| 49 | *Ordinal Only* | `0xD230` | 791 | UnwindData |  |
| 147 | `MessageBoxInstW` | `0xD550` | 117 | UnwindData |  |
| 215 | *Ordinal Only* | `0xD5D0` | 50 | UnwindData |  |
| 214 | *Ordinal Only* | `0xD610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `RicheditStreamIn` | `0xD620` | 129 | UnwindData |  |
| 184 | `RicheditStreamOut` | `0xD6B0` | 121 | UnwindData |  |
| 65 | *Ordinal Only* | `0xD730` | 174 | UnwindData |  |
| 43 | *Ordinal Only* | `0xD7F0` | 36 | UnwindData |  |
| 42 | *Ordinal Only* | `0xD820` | 36 | UnwindData |  |
| 185 | `ShellUtil_GetSpecialFolderPath` | `0xD850` | 110 | UnwindData |  |
| 195 | `UpdateRebarBandColors` | `0xD8D0` | 290 | UnwindData |  |
| 6 | *Ordinal Only* | `0xDA00` | 125 | UnwindData |  |
| 69 | *Ordinal Only* | `0xDA90` | 134 | UnwindData |  |
| 5 | *Ordinal Only* | `0xDB20` | 67 | UnwindData |  |
| 68 | *Ordinal Only* | `0xDB70` | 69 | UnwindData |  |
| 197 | `WriteStreamToFileHandle` | `0xDBC0` | 213 | UnwindData |  |
| 202 | `fGetBrowserUrlEncoding` | `0xDCA0` | 138 | UnwindData |  |
| 113 | `HrCreatePhonebookEntry` | `0xDD30` | 262 | UnwindData |  |
| 116 | `HrEditPhonebookEntryW` | `0xDE40` | 252 | UnwindData |  |
| 117 | `HrFillRasCombo` | `0xDF50` | 477 | UnwindData |  |
| 20 | `GetRichEdClassStringW` | `0xE290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `SetFontOnRichEd` | `0xE2C0` | 148 | UnwindData |  |
| 155 | *Ordinal Only* | `0xE3C0` | 554 | UnwindData |  |
| 153 | *Ordinal Only* | `0xE5F0` | 496 | UnwindData |  |
| 151 | *Ordinal Only* | `0xE7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | *Ordinal Only* | `0xE810` | 1,036 | UnwindData |  |
| 154 | *Ordinal Only* | `0xEC30` | 264 | UnwindData |  |
| 158 | *Ordinal Only* | `0xED40` | 193 | UnwindData |  |
| 156 | *Ordinal Only* | `0xEE10` | 177 | UnwindData |  |
| 152 | *Ordinal Only* | `0xEED0` | 264 | UnwindData |  |
| 210 | *Ordinal Only* | `0xEFE0` | 164 | UnwindData |  |
| 211 | *Ordinal Only* | `0xF230` | 118 | UnwindData |  |
| 38 | *Ordinal Only* | `0xF800` | 103 | UnwindData |  |
| 81 | `CreateStreamOnHFile` | `0xF870` | 254 | UnwindData |  |
| 82 | `CreateStreamOnHFileW` | `0xF980` | 300 | UnwindData |  |
| 84 | `CreateTempFileStream` | `0xFAC0` | 174 | UnwindData |  |
| 108 | `HrCopyLockBytesToStream` | `0xFB80` | 189 | UnwindData |  |
| 109 | `HrCopyStream` | `0xFC50` | 186 | UnwindData |  |
| 110 | `HrCopyStreamCB` | `0xFD10` | 306 | UnwindData |  |
| 111 | `HrCopyStreamCBEndOnCRLF` | `0xFE50` | 348 | UnwindData |  |
| 112 | `HrCopyStreamToByte` | `0xFFC0` | 211 | UnwindData |  |
| 123 | `HrGetStreamPos` | `0x100A0` | 74 | UnwindData |  |
| 124 | `HrGetStreamSize` | `0x100F0` | 74 | UnwindData |  |
| 130 | `HrIsStreamUnicode` | `0x10140` | 170 | UnwindData |  |
| 133 | `HrRewindStream` | `0x101F0` | 43 | UnwindData |  |
| 136 | `HrStreamSeekBegin` | `0x101F0` | 43 | UnwindData |  |
| 134 | `HrSafeGetStreamSize` | `0x10230` | 118 | UnwindData |  |
| 137 | `HrStreamSeekCur` | `0x102B0` | 32 | UnwindData |  |
| 138 | `HrStreamSeekEnd` | `0x102E0` | 44 | UnwindData |  |
| 139 | `HrStreamSeekSet` | `0x10320` | 30 | UnwindData |  |
| 140 | `HrStreamToByte` | `0x10350` | 184 | UnwindData |  |
| 148 | `OpenFileStream` | `0x10410` | 206 | UnwindData |  |
| 149 | `OpenFileStreamShare` | `0x104F0` | 223 | UnwindData |  |
| 161 | `OpenFileStreamW` | `0x105E0` | 26 | UnwindData |  |
| 162 | `OpenFileStreamWithFlagsW` | `0x10600` | 56 | UnwindData |  |
| 189 | `StreamSubStringMatchW` | `0x10640` | 524 | UnwindData |  |
| 196 | `WriteStreamToFile` | `0x10860` | 196 | UnwindData |  |
| 198 | `WriteStreamToFileW` | `0x10930` | 171 | UnwindData |  |
| 35 | `StrTokExA` | `0x109F0` | 219 | UnwindData |  |
| 72 | `CleanupFileNameInPlaceA` | `0x10AE0` | 182 | UnwindData |  |
| 73 | `CleanupFileNameInPlaceW` | `0x10BA0` | 155 | UnwindData |  |
| 92 | `FIsEmptyA` | `0x10C50` | 52 | UnwindData |  |
| 96 | `FIsSpaceA` | `0x10C90` | 97 | UnwindData |  |
| 98 | `FIsValidFileNameCharA` | `0x10D00` | 110 | UnwindData |  |
| 99 | `FIsValidFileNameCharW` | `0x10D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `HrFindInetTimeZone` | `0x10DB0` | 123 | UnwindData |  |
| 143 | `IsPrint` | `0x10E40` | 99 | UnwindData |  |
| 144 | `IsUpper` | `0x10EB0` | 93 | UnwindData |  |
| 145 | `IsValidFileIfFileUrlW` | `0x10F20` | 165 | UnwindData |  |
| 167 | `PszAllocW` | `0x10FD0` | 67 | UnwindData |  |
| 168 | `PszDayFromIndex` | `0x11020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `PszDupW` | `0x11040` | 104 | UnwindData |  |
| 171 | `PszEscapeMenuStringA` | `0x110B0` | 139 | UnwindData |  |
| 172 | `PszEscapeMenuStringW` | `0x11150` | 98 | UnwindData |  |
| 173 | `PszFromANSIStreamA` | `0x111C0` | 156 | UnwindData |  |
| 174 | `PszMonthFromIndex` | `0x11270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | *Ordinal Only* | `0x11290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `PszScanToWhiteA` | `0x112B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | *Ordinal Only* | `0x112D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `PszSkipWhiteA` | `0x11300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `PszSkipWhiteW` | `0x11320` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `ReplaceChars` | `0x11350` | 101 | UnwindData |  |
| 182 | `ReplaceCharsW` | `0x113C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `StrToUintA` | `0x113F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `StrToUintW` | `0x11420` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `StrTokExW` | `0x11460` | 221 | UnwindData |  |
| 190 | `StripCRLF` | `0x11550` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `UlStripWhitespace` | `0x115B0` | 249 | UnwindData |  |
| 193 | `UlStripWhitespaceW` | `0x116B0` | 285 | UnwindData |  |
| 199 | `_MSG` | `0x117E0` | 157 | UnwindData |  |
| 203 | `strtrim` | `0x11890` | 122 | UnwindData |  |
| 204 | `strtrimW` | `0x11910` | 139 | UnwindData |  |
| 31 | `IVoidPtrList_CreateInstance` | `0x11D00` | 53 | UnwindData |  |
| 30 | `IUnknownList_CreateInstance` | `0x12380` | 53 | UnwindData |  |
| 194 | `UnlocStrEqNW` | `0x12470` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | *Ordinal Only* | `0x124C0` | 101 | UnwindData |  |
| 45 | *Ordinal Only* | `0x12530` | 142 | UnwindData |  |
| 18 | *Ordinal Only* | `0x125D0` | 448 | UnwindData |  |
| 21 | *Ordinal Only* | `0x127A0` | 148 | UnwindData |  |
| 22 | *Ordinal Only* | `0x12840` | 54 | UnwindData |  |
| 26 | *Ordinal Only* | `0x12880` | 378 | UnwindData |  |
| 24 | *Ordinal Only* | `0x12A00` | 215 | UnwindData |  |
| 27 | *Ordinal Only* | `0x12AE0` | 100 | UnwindData |  |
| 25 | *Ordinal Only* | `0x12B50` | 285 | UnwindData |  |
