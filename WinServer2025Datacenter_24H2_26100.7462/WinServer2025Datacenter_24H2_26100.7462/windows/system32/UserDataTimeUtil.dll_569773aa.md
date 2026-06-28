# Binary Specification: UserDataTimeUtil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UserDataTimeUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `569773aa9261b1507cb737b29edf62f542f92650769b187fda4e03a4c879a8c3`
* **Total Exported Functions:** 48

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetDaysForMonth` | `0x1D70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `LIncrWord` | `0x1DF0` | 86 | UnwindData |  |
| 6 | `CmpDateST` | `0x1E50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CmpST` | `0x1EA0` | 97 | UnwindData |  |
| 8 | `CmpYMD` | `0x1F10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DaysBetweenDates` | `0x1F60` | 544 | UnwindData |  |
| 15 | `DaysBetweenFT` | `0x2190` | 130 | UnwindData |  |
| 16 | `DowFromDate` | `0x2220` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `DurationBetweenFT` | `0x2330` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `GetStartEndTime` | `0x23A0` | 150 | UnwindData |  |
| 32 | `IncrSystemTime` | `0x2440` | 723 | UnwindData |  |
| 38 | `MinutesBetweenFT` | `0x2720` | 136 | UnwindData |  |
| 39 | `MinutesBetweenST` | `0x27B0` | 147 | UnwindData |  |
| 41 | `PimGetDateFormat` | `0x2850` | 290 | UnwindData |  |
| 45 | `RoundEventTime` | `0x2980` | 238 | UnwindData |  |
| 46 | `SecondsBetweenFT` | `0x2A80` | 141 | UnwindData |  |
| 3 | `AdjustForAllDayAppts` | `0x2E40` | 223 | UnwindData |  |
| 4 | `AdjustForBias` | `0x2F30` | 363 | UnwindData |  |
| 5 | `AdjustGMTForAllDayAppts` | `0x30B0` | 131 | UnwindData |  |
| 9 | `ConvertFileTimeToLocalVariantTime` | `0x3140` | 152 | UnwindData |  |
| 10 | `ConvertLocalVariantTimeToFileTime` | `0x31E0` | 152 | UnwindData |  |
| 11 | `ConvertSchedPlusToRenTz` | `0x3280` | 438 | UnwindData |  |
| 12 | `ConvertTimeZone` | `0x3440` | 239 | UnwindData |  |
| 13 | `ConvertVariantTimeToFileTime` | `0x3540` | 190 | UnwindData |  |
| 19 | `FileTimeAdjustTzToUTC` | `0x3610` | 186 | UnwindData |  |
| 20 | `FileTimeAdjustUTCToTz` | `0x36D0` | 186 | UnwindData |  |
| 21 | `FileTimeToLocalFileTimeEx` | `0x3790` | 227 | UnwindData |  |
| 22 | `FileTimeToTzSpecificVariantTime` | `0x3880` | 173 | UnwindData |  |
| 23 | `FileTimeToVariantTime` | `0x3940` | 118 | UnwindData |  |
| 34 | `LegacyTimezoneInformationToTimezoneInformation` | `0x39C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `LocalFileTimeToFileTimeEx` | `0x39F0` | 227 | UnwindData |  |
| 44 | `RenFromStdTimeZoneInfo` | `0x3AE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `StdTimeZoneInfoFromRen` | `0x3B10` | 81 | UnwindData |  |
| 18 | `ExpandRtm` | `0x3B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `TruncFt` | `0x3B90` | 123 | UnwindData |  |
| 24 | `GetCurrentLocalTime` | `0x3C20` | 121 | UnwindData |  |
| 40 | `PimGet24HourFormat` | `0x3CA0` | 85 | UnwindData |  |
| 42 | `PimGetLocaleInfo` | `0x3D00` | 147 | UnwindData |  |
| 43 | `PimGetTimeFormat` | `0x3DA0` | 214 | UnwindData |  |
| 25 | `GetDaysForLunarMonthOfCalendar` | `0x4630` | 40 | UnwindData |  |
| 26 | `GetLeapMonthOfLunarYear` | `0x4660` | 86 | UnwindData |  |
| 28 | `GetLunarDate` | `0x46C0` | 104 | UnwindData |  |
| 29 | `GetLunarDateOfCalendar` | `0x4730` | 130 | UnwindData |  |
| 30 | `GetSolarDateOfCalendar` | `0x47C0` | 130 | UnwindData |  |
| 33 | `IsSupportedLunarCalendarType` | `0x4850` | 78 | UnwindData |  |
| 27 | `GetLocalIANAName` | `0x6150` | 277 | UnwindData |  |
| 36 | `MapIANATZNameToTZInfo` | `0x6270` | 618 | UnwindData |  |
| 37 | `MapTZInfoToIANAName` | `0x64E0` | 1,031 | UnwindData |  |
