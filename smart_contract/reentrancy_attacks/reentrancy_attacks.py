import subprocess
import os


def check_reentrancy_with_slither(contract_path):
    """
    使用 Slither 检查合约的重入攻击漏洞。
    """
    print(f"Checking for reentrancy vulnerabilities in {contract_path} with Slither...")
    try:
        result = subprocess.run(["slither", contract_path, "--detect", "reentrancy-vulnerability"],
                                capture_output=True, text=True)
        if "Reentrancy in" in result.stdout:
            print("Potential reentrancy vulnerability found!")
            print(result.stdout)
        else:
            print("No reentrancy vulnerability found.")
    except Exception as e:
        print(f"An error occurred while running Slither: {e}")


def check_reentrancy_with_mythril(contract_path):
    """
    使用 Mythril 检查合约的重入攻击漏洞。
    """
    print(f"Checking for reentrancy vulnerabilities in {contract_path} with Mythril...")
    try:
        print(0)
        result = subprocess.run(["myth", "analyze", contract_path, "-v", "2"],
                                capture_output=True, text=True)
        print(1)
        if "Reentrancy" in result.stdout:
            print(2)
            print("Potential reentrancy vulnerability found!")
            print(result.stdout)
        else:
            print(2)
            print("No reentrancy vulnerability found.")
    except Exception as e:
        print(f"An error occurred while running Mythril: {e}")


def main():
    contract_path = "./VulnerableContract.sol"  # 指定智能合约文件路径

    # 检查文件是否存在
    if not os.path.exists(contract_path):
        print(f"Contract file not found: {contract_path}")
        return

    # 使用 Slither 检查重入攻击漏洞
    check_reentrancy_with_slither(contract_path)

    # 使用 Mythril 检查重入攻击漏洞
    check_reentrancy_with_mythril(contract_path)


if __name__ == "__main__":
    main()
