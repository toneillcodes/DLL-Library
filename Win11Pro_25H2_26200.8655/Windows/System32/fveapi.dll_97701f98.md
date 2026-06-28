# Binary Specification: fveapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fveapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `97701f989fb72cba195fdbca4d0054a9995396aa51a5d7034e3bba05c75e69fc`
* **Total Exported Functions:** 162

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 81 | `FveGetDataSetEx` | `0x5280` | 245 | UnwindData |  |
| 12 | `FveAddAuthMethodInformation` | `0x5380` | 352 | UnwindData |  |
| 145 | `FveSysClearUserFlags` | `0x54F0` | 184 | UnwindData |  |
| 80 | `FveGetDataSet` | `0x55B0` | 233 | UnwindData |  |
| 83 | `FveGetDeviceLockoutData` | `0x56A0` | 201 | UnwindData |  |
| 105 | `FveIsBoundDataVolumeToOSVolume` | `0x5770` | 251 | UnwindData |  |
| 104 | `FveIsBoundDataVolume` | `0x5880` | 251 | UnwindData |  |
| 107 | `FveIsDeviceLockedOut` | `0x5990` | 183 | UnwindData |  |
| 133 | `FveSelectBestRecoveryPasswordByBackupInformation` | `0x5A50` | 185 | UnwindData |  |
| 86 | `FveGetFveMethod` | `0xC8C0` | 254 | UnwindData |  |
| 90 | `FveGetIdentity` | `0xD7A0` | 245 | UnwindData |  |
| 88 | `FveGetFveMethodEx` | `0xD8A0` | 285 | UnwindData |  |
| 70 | `FveFindNextVolume` | `0xDAC0` | 230 | UnwindData |  |
| 115 | `FveIsVolumeEncryptable` | `0xDBB0` | 210 | UnwindData |  |
| 122 | `FveOpenVolumeByHandle` | `0xDC90` | 766 | UnwindData |  |
| 124 | `FveOpenVolumeW` | `0xE800` | 34 | UnwindData |  |
| 40 | `FveCloseVolume` | `0xE830` | 173 | UnwindData |  |
| 98 | `FveGetVolumeNameW` | `0xE8F0` | 951 | UnwindData |  |
| 39 | `FveCloseHandle` | `0xECB0` | 233 | UnwindData |  |
| 95 | `FveGetStatus` | `0xEDA0` | 298 | UnwindData |  |
| 123 | `FveOpenVolumeExW` | `0xF430` | 922 | UnwindData |  |
| 135 | `FveSetAllowKeyExport` | `0x11B80` | 201 | UnwindData |  |
| 6 | `NgscbCheckIsAOACDevice` | `0x15B50` | 252 | UnwindData |  |
| 36 | `FveCheckTpmCapability` | `0x1C020` | 196 | UnwindData |  |
| 73 | `FveGenerateNkpSessionKeys` | `0x1C4B0` | 212 | UnwindData |  |
| 129 | `FveRegenerateNbpSessionKey` | `0x1C6E0` | 212 | UnwindData |  |
| 16 | `FveApplyNkpCertChanges` | `0x1D010` | 212 | UnwindData |  |
| 76 | `FveGetAuthMethodInformation` | `0x1E830` | 284 | UnwindData |  |
| 7 | `NgscbCheckIsHSTIVerified` | `0x2E2D0` | 261 | UnwindData |  |
| 127 | `FveQueryDeviceEncryptionSupport` | `0x31460` | 586 | UnwindData |  |
| 74 | `FveGetAllowKeyExport` | `0x34560` | 177 | UnwindData |  |
| 32 | `FveCanStandardUsersChangePin` | `0x37730` | 129 | UnwindData |  |
| 15 | `FveApplyGroupPolicy` | `0x37DC0` | 212 | UnwindData |  |
| 147 | `FveSysGetUserFlags` | `0x3A6A0` | 228 | UnwindData |  |
| 69 | `FveFindFirstVolume` | `0x3AB80` | 279 | UnwindData |  |
| 31 | `FveCanStandardUsersChangePassphraseByProxy` | `0x3B330` | 241 | UnwindData |  |
| 96 | `FveGetStatusW` | `0x3BB00` | 524 | UnwindData |  |
| 94 | `FveGetSecureBootBindingState` | `0x3D4E0` | 337 | UnwindData |  |
| 146 | `FveSysCloseVolume` | `0x3E510` | 127 | UnwindData |  |
| 149 | `FveSysSetUserFlags` | `0x3E600` | 247 | UnwindData |  |
| 155 | `FveUpdateBandIdBcd` | `0x3ECC0` | 212 | UnwindData |  |
| 75 | `FveGetAuthMethodGuids` | `0x40960` | 284 | UnwindData |  |
| 11 | `NgscbIsHostOsOnRoamableDrive` | `0x41680` | 70 | UnwindData |  |
| 71 | `FveFlagsToProtectorType` | `0x41B30` | 141 | UnwindData |  |
| 125 | `FveProtectorTypeToFlags` | `0x41CE0` | 141 | UnwindData |  |
| 4 | `NgscbCheckDmaSecurityEx` | `0x41FC0` | 243 | UnwindData |  |
| 23 | `FveAuthElementToRecoveryPasswordW` | `0x454B0` | 188 | UnwindData |  |
| 5 | `NgscbCheckHSTIPrerequisitesVerified` | `0x47050` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `FveIsDeviceLockable` | `0x47430` | 247 | UnwindData |  |
| 77 | `FveGetAuthMethodSid` | `0x507C0` | 216 | UnwindData |  |
| 137 | `FveSetFipsAllowDisabled` | `0x50DB0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NgscbCheckDmaSecurity` | `0x50F20` | 20,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InternalFveIsVolumeEncrypted` | `0x55EF0` | 234 | UnwindData |  |
| 18 | `FveAuthElementFromPassPhraseW` | `0x56700` | 165 | UnwindData |  |
| 19 | `FveAuthElementFromPinW` | `0x567B0` | 194 | UnwindData |  |
| 20 | `FveAuthElementFromRecoveryPasswordW` | `0x56880` | 165 | UnwindData |  |
| 21 | `FveAuthElementGetKeyFileNameW` | `0x56930` | 188 | UnwindData |  |
| 22 | `FveAuthElementReadExternalKeyW` | `0x56A00` | 208 | UnwindData |  |
| 24 | `FveAuthElementWriteExternalKeyExW` | `0x56AE0` | 188 | UnwindData |  |
| 25 | `FveAuthElementWriteExternalKeyW` | `0x56BB0` | 178 | UnwindData |  |
| 30 | `FveCanPinExceptionPolicyBeApplied` | `0x56C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `FveClearRecoveryPasswordBackupInformation` | `0x56C80` | 218 | UnwindData |  |
| 38 | `FveClearUserFlags` | `0x56D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `FveGetUserFlags` | `0x56D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `FveSetUserFlags` | `0x56D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `FveCommitChanges` | `0x56D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `FveCommitChangesEx` | `0x56D80` | 277 | UnwindData |  |
| 44 | `FveConversionDecrypt` | `0x56EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `FveConversionDecryptEx` | `0x56EB0` | 220 | UnwindData |  |
| 50 | `FveConversionPause` | `0x56FA0` | 204 | UnwindData |  |
| 51 | `FveConversionResume` | `0x57080` | 204 | UnwindData |  |
| 52 | `FveConversionStop` | `0x57160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `FveConversionStopEx` | `0x57170` | 222 | UnwindData |  |
| 58 | `FveDiscardChanges` | `0x57260` | 177 | UnwindData |  |
| 60 | `FveEnableRawAccess` | `0x57320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `FveEnableRawAccessEx` | `0x57330` | 205 | UnwindData |  |
| 62 | `FveEnableRawAccessW` | `0x57410` | 207 | UnwindData |  |
| 63 | `FveEraseDrive` | `0x574F0` | 200 | UnwindData |  |
| 65 | `FveExternalDataCreateEntry` | `0x575C0` | 228 | UnwindData |  |
| 66 | `FveExternalDataDeleteEntries` | `0x576B0` | 201 | UnwindData |  |
| 67 | `FveExternalDataGetEntryInfo` | `0x57780` | 257 | UnwindData |  |
| 68 | `FveExternalDataGetEntryRawData` | `0x57890` | 228 | UnwindData |  |
| 85 | `FveGetFipsAllowDisabled` | `0x57980` | 152 | UnwindData |  |
| 87 | `FveGetFveMethodEDrv` | `0x57A20` | 213 | UnwindData |  |
| 91 | `FveGetKeyPackage` | `0x57B00` | 255 | UnwindData |  |
| 92 | `FveGetRecoveryPasswordBackupAccountInformation` | `0x57C10` | 238 | UnwindData |  |
| 93 | `FveGetRecoveryPasswordBackupInformation` | `0x57D10` | 201 | UnwindData |  |
| 108 | `FveIsHardwareReadyForConversion` | `0x57DE0` | 120 | UnwindData |  |
| 111 | `FveIsPassphraseCompatibleW` | `0x57E60` | 183 | UnwindData |  |
| 112 | `FveIsRecoveryPasswordGroupValidW` | `0x57F20` | 165 | UnwindData |  |
| 113 | `FveIsRecoveryPasswordValidW` | `0x57FD0` | 165 | UnwindData |  |
| 118 | `FveLockVolume` | `0x58080` | 200 | UnwindData |  |
| 121 | `FveNotifyVolumeAfterFormat` | `0x58150` | 167 | UnwindData |  |
| 131 | `FveRevertVolume` | `0x58200` | 167 | UnwindData |  |
| 132 | `FveSaveRecoveryPasswordBackupFlag` | `0x582B0` | 109 | UnwindData |  |
| 138 | `FveSetFveMethod` | `0x58330` | 181 | UnwindData |  |
| 139 | `FveSetFveMethodEx` | `0x583F0` | 216 | UnwindData |  |
| 141 | `FveSetRecoveryPasswordBackupAccountInformation` | `0x584D0` | 228 | UnwindData |  |
| 142 | `FveSetRecoveryPasswordBackupInformation` | `0x585C0` | 240 | UnwindData |  |
| 159 | `FveUpgradeVolume` | `0x586C0` | 167 | UnwindData |  |
| 1 | `FvePpfPredictionsUpdated` | `0x58DC0` | 1,443 | UnwindData |  |
| 13 | `FveAddAuthMethodSid` | `0x59C00` | 318 | UnwindData |  |
| 17 | `FveAttemptAutoUnlock` | `0x59D50` | 204 | UnwindData |  |
| 26 | `FveBackupRecoveryInformationToAAD` | `0x59E30` | 183 | UnwindData |  |
| 27 | `FveBackupRecoveryInformationToAD` | `0x59EF0` | 209 | UnwindData |  |
| 28 | `FveBackupRecoveryInformationToADEx` | `0x59FD0` | 272 | UnwindData |  |
| 29 | `FveBindDataVolume` | `0x5A0F0` | 239 | UnwindData |  |
| 33 | `FveCheckADRecoveryInfoBackupPolicy` | `0x5A1F0` | 195 | UnwindData |  |
| 34 | `FveCheckADRecoveryInfoBackupPolicyEx` | `0x5A2C0` | 298 | UnwindData |  |
| 35 | `FveCheckPassphrasePolicy` | `0x5A3F0` | 183 | UnwindData |  |
| 43 | `FveControl` | `0x5A4B0` | 182 | UnwindData |  |
| 46 | `FveConversionEncrypt` | `0x5A570` | 127 | UnwindData |  |
| 47 | `FveConversionEncryptEx` | `0x5A600` | 181 | UnwindData |  |
| 48 | `FveConversionEncryptPendingReboot` | `0x5A6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `FveConversionEncryptPendingRebootEx` | `0x5A6D0` | 181 | UnwindData |  |
| 54 | `FveDecrementClearKeyCounter` | `0x5A790` | 167 | UnwindData |  |
| 55 | `FveDeleteAuthMethod` | `0x5A840` | 218 | UnwindData |  |
| 56 | `FveDeleteDeviceEncryptionOptOutForVolumeW` | `0x5A920` | 315 | UnwindData |  |
| 57 | `FveDisableDeviceLockoutState` | `0x5AA70` | 185 | UnwindData |  |
| 59 | `FveDraCertPresentInRegistry` | `0x5AB30` | 144 | UnwindData |  |
| 64 | `FveEscrowEncryptedRecoveryKeyForRetailUnlock` | `0x5ABD0` | 143 | UnwindData |  |
| 72 | `FveGenerateNbp` | `0x5AC70` | 199 | UnwindData |  |
| 78 | `FveGetAuthMethodSidInformation` | `0x5AD40` | 374 | UnwindData |  |
| 79 | `FveGetClearKeyCounter` | `0x5AEC0` | 183 | UnwindData |  |
| 82 | `FveGetDescriptionW` | `0x5AF80` | 238 | UnwindData |  |
| 84 | `FveGetExternalKeyBlob` | `0x5B080` | 165 | UnwindData |  |
| 89 | `FveGetIdentificationFieldW` | `0x5B130` | 238 | UnwindData |  |
| 99 | `FveInitVolume` | `0x5B230` | 144 | UnwindData |  |
| 100 | `FveInitVolumeEx` | `0x5B2D0` | 217 | UnwindData |  |
| 101 | `FveInitializeDeviceEncryption` | `0x5B3B0` | 573 | UnwindData |  |
| 102 | `FveInitializeDeviceEncryption2` | `0x5B600` | 415 | UnwindData |  |
| 103 | `FveIsAnyDataVolumeBoundToOSVolume` | `0x5B7B0` | 195 | UnwindData |  |
| 109 | `FveIsHybridVolume` | `0x5B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `FveIsHybridVolumeW` | `0x5B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `FveNeedsDiscoveryVolumeUpdate` | `0x5B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `FveServiceDiscoveryVolume` | `0x5B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `FveIsSchemaExtInstalled` | `0x5B890` | 144 | UnwindData |  |
| 116 | `FveKeyManagement` | `0x5B930` | 284 | UnwindData |  |
| 117 | `FveLockDevice` | `0x5BA60` | 167 | UnwindData |  |
| 119 | `FveLogRecoveryReason` | `0x5BB10` | 216 | UnwindData |  |
| 126 | `FveQuery` | `0x5BBF0` | 182 | UnwindData |  |
| 128 | `FveRecalculateOffsetsAndMoveMetadata` | `0x5BCB0` | 268 | UnwindData |  |
| 130 | `FveResetTpmDictionaryAttackParameters` | `0x5BDD0` | 263 | UnwindData |  |
| 136 | `FveSetDescriptionW` | `0x5BEE0` | 221 | UnwindData |  |
| 140 | `FveSetIdentificationFieldW` | `0x5BFD0` | 227 | UnwindData |  |
| 148 | `FveSysOpenVolumeW` | `0x5C0C0` | 159 | UnwindData |  |
| 150 | `FveUnbindAllDataVolumeFromOSVolume` | `0x5C170` | 1,153 | UnwindData |  |
| 151 | `FveUnbindDataVolume` | `0x5C600` | 190 | UnwindData |  |
| 152 | `FveUnlockVolume` | `0x5C6D0` | 304 | UnwindData |  |
| 153 | `FveUnlockVolumeAuthMethodSid` | `0x5C810` | 277 | UnwindData |  |
| 154 | `FveUnlockVolumeWithAccessMode` | `0x5C930` | 380 | UnwindData |  |
| 156 | `FveUpdateDeviceLockoutState` | `0x5CAC0` | 163 | UnwindData |  |
| 157 | `FveUpdateDeviceLockoutStateEx` | `0x5CB70` | 234 | UnwindData |  |
| 158 | `FveUpdatePinW` | `0x5CC60` | 238 | UnwindData |  |
| 160 | `FveValidateDeviceLockoutState` | `0x5CD60` | 167 | UnwindData |  |
| 161 | `FveValidateExistingPassphraseW` | `0x5CE10` | 239 | UnwindData |  |
| 162 | `FveValidateExistingPinW` | `0x5CF10` | 239 | UnwindData |  |
| 14 | `FveAddPredictiveTpmProtector` | `0x5D210` | 1,054 | UnwindData |  |
| 144 | `FveSetupTpmCallback` | `0x5D640` | 996 | UnwindData |  |
| 8 | `NgscbCheckPreventDeviceEncryption` | `0xAF2C0` | 173 | UnwindData |  |
| 9 | `NgscbCheckPreventDeviceEncryptionForAad` | `0xAF380` | 173 | UnwindData |  |
| 10 | `NgscbGetWinReConfiguration` | `0xAF780` | 509 | UnwindData |  |
